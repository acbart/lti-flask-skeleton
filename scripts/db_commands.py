from flask_script import Command, Option
from flask_security.utils import encrypt_password
from models.models import db
from main import app
import datetime
import random
import json
from pprint import pprint

class CreateDB(Command):
    def run(self, **kwargs):
        print(db.engine)
        print(dir(db.engine))
        db.engine.echo = True
        r = db.create_all()
        print(r)
class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        db.drop_all()
        db.create_all()
        
class PopulateDB(Command):
    option_list = (
        Option('--file', '-f', dest='user_data_file', default='scripts/user_data.csv'),
    )
    
    """Fills in predefined data into DB"""
    def run(self, user_data_file, **kwargs):
        from models.models import Role, User, Course, Assignment, CourseAssignment, AssignmentGroup, AssignmentGroupMembership
        
        print("Adding Admin")
        admin = User(first_name='Cory', last_name='Bart', 
                     password=encrypt_password('password'),
                     confirmed_at=datetime.datetime.now(),
                     active= True,
                     email='acbart@vt.edu', gender='Male')
        db.session.add(admin)
        db.session.flush()
        db.session.add(Role(name='instructor', user_id=admin.id))
        db.session.add(Role(name='admin', user_id=admin.id))
        
        print("Adding some students for color")
        for student in ('Dan Tilden', 'Anamary Leal', 'Ellie Cayford'):
            first, last = student.split()
            email = '{}{}@vt.edu'.format(first[0].lower(), last.lower())
            user = User(first_name=first, last_name=last, email=email)
            db.session.add(user)
            
        print("Adding default course")
        default_course = Course(name="Computational Thinking", owner_id=admin.id, service="native")
        db.session.add(default_course)
        db.session.flush()
        
        print("Adding public course")
        public_course = Course(name="Public Course", owner_id=admin.id, service="native", visibility='public')
        db.session.add(public_course)
        db.session.flush()
        db.session.add(Role(name='instructor', course_id=public_course.id, user_id=admin.id))
        
        print("Adding local Canvas course")
        canvas_course = Course(name="Computational Thinking - Dev", owner_id=admin.id, service='canvas', visibility='private', external_id='cbdd860576c6c08ccb998b93009305c318bd269b')
        db.session.add(canvas_course)
        db.session.flush()
        
        print("Adding CS1 course")
        cs1_course = Course(name="CS 1", owner_id=user.id, service='canvas', visibility='private')
        db.session.add(cs1_course)
        db.session.flush()
        
        print("Adding some assignments")
        assignment1 = Assignment(name="Assignment #1", body="a=b+c", 
                                 course_id=default_course.id, owner_id=admin.id)
        db.session.add(assignment1)
        assignment2 = Assignment(name="Assignment #2", body="Figure it out!", 
                                 course_id=default_course.id, owner_id=admin.id)
        db.session.add(assignment2)
        assignment3 = Assignment(name="Assignment #3", body="Clue", 
                                 course_id=default_course.id, owner_id=admin.id)
        db.session.add(assignment3)
        
        ca1 = CourseAssignment(course_id=public_course.id, assignment_id=assignment1.id)
        db.session.add(ca1)
        ca2 = CourseAssignment(course_id=public_course.id, assignment_id=assignment2.id)
        db.session.add(ca2)
        
        ag1 = AssignmentGroup(name="Day 1 - Decision", course_id=default_course.id)
        db.session.add(ag1)
        ag2 = AssignmentGroup(name="Day 2 - Iteration", course_id=default_course.id)
        db.session.add(ag2)
        db.session.commit()
        
        db.session.add(AssignmentGroupMembership(assignment_group_id=ag1.id, assignment_id=assignment1.id))
        db.session.add(AssignmentGroupMembership(assignment_group_id=ag1.id, assignment_id=assignment2.id))
        db.session.add(AssignmentGroupMembership(assignment_group_id=ag2.id, assignment_id=assignment3.id))
        
        db.session.commit()
        print("Complete")
        

class DisplayDB(Command):
    def run(self, **kwargs):
        from sqlalchemy import MetaData
        from sqlalchemy_schemadisplay3 import create_schema_graph
        connection = app.config['SQLALCHEMY_DATABASE_URI']
        filename='dbschema.png'
        graph = create_schema_graph(metadata=MetaData(connection),
            show_datatypes=True, # The image would get nasty big if we'd show the datatypes
            show_indexes=False, # ditto for indexes
            rankdir='LR', # From left to right (instead of top to bottom)
            font='Helvetica',
            concentrate=False # Don't try to join the relation lines together
            )
        graph.write_png(filename) # write out the file
