'''
Your admin controller should hold routes that let administrators do their job.
For instance, I create views into the database using FlaskAdmin, and also
have a route for remotely shutting down my server.
'''

# Import Flask
from flask import g, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from jinja2 import Markup

# Import runestone
from main import app
from controllers.helpers import admin_required
from models.models import (User, db, Course, Submission, Assignment, 
                           AssignmentGroup, AssignmentGroupMembership, Settings,
                           Authentication, Role)

admin = Admin(app)

class RequireAdminView(ModelView):
    '''
    A simple View that demands the the user be an admin.
    '''
    def is_accessible(self):
        if g.user:
            return g.user.is_admin()
        return False
        
class UserView(RequireAdminView):
    '''
    An override of the basic view for users, hiding their password and displaying
    an image for them.
    '''
    def _list_thumbnail(view, context, model, name):
        if model.picture.startswith('http'):
            return Markup('<img style="width:50px" src="{}">'.format(model.picture))
        else:
            return Markup('<img src="{}">'.format(url_for('static', filename='images/anon.jpg')))
    column_formatters = { 'picture': _list_thumbnail}
    form_excluded_columns = ('password',)
    column_exclude_list = ('password',)
    column_display_pk = True

class ModelIdView(RequireAdminView):
    '''
    A simple adjustment of the basic view to show the primary key.
    '''
    column_display_pk = True
    
def _editable(table, field):
    def _edit_field(view, context, model, name):
        return table.query.filter(getattr(table, field) == getattr(model, name)).first()
    return _edit_field
    
def _id(table):
    def _edit_id(view, context, model, name):
        return table.query.filter(table.id == getattr(model, name)).first()
    return _edit_id
    
class RoleView(RequireAdminView):
    column_list = ('id', 'date_created', 'name', 'user_id', 'course_id')
    column_labels = {'id': 'Role ID', 'date_created': 'Created',
                     'name': 'Name', 'user_id': "User", "course_id": "Course"}
    column_searchable_list = ('name', 'course_id', 'user_id')
    column_sortable_list = ('id', 'date_created', 'name', 'user_id', 'course_id')
    column_formatters = { 'user_id': _id(User),
                          'course_id': _id(Course)}
    form_columns = ('name', 'user_id', 'course_id')
class AssignmentView(RequireAdminView):
    column_list = ('id', 'date_modified', 
                   'owner_id', 'course_id',
                   'name', 'body', 
                   'on_run', 'on_start', 'answer', 
                   'type', 'visibility', 'disabled', 'mode',
                   'version'
                   )
class AssignmentGroupView(RequireAdminView):
    column_list = ('id', 'date_modified', 
                   'owner_id', 'course_id',
                   'name'
                   )
class AssignmentGroupMembershipView(RequireAdminView):
    column_list = ('id', 'date_modified', 
                   'assignment_group_id', 'assignment_id',
                   'position'
                   )
    form_columns = ('assignment_group_id', 'assignment_id', 'position')
    column_formatters = { 'user_id': _editable(User, 'id'),
                          'course_id': _editable(Course, 'id')}
class SubmissionView(RequireAdminView):
    column_list = ('id', 'date_modified', 
                   'user_id', 'assignment_id',
                   'code', 'status', 
                   'correct', 'version', 'assignment_version'
                   )
                   
'''
Register the actual views themselves..
'''
admin.add_view(UserView(User, db.session, category='Tables'))
admin.add_view(ModelIdView(Course, db.session, category='Tables'))
admin.add_view(SubmissionView(Submission, db.session, category='Tables'))
admin.add_view(AssignmentView(Assignment, db.session, category='Tables'))
admin.add_view(AssignmentGroupView(AssignmentGroup, db.session, category='Tables'))
admin.add_view(AssignmentGroupMembershipView(AssignmentGroupMembership, db.session, category='Tables'))
admin.add_view(ModelIdView(Settings, db.session, category='Tables'))
admin.add_view(ModelIdView(Authentication, db.session, category='Tables'))
admin.add_view(RoleView(Role, db.session, category='Tables'))

@app.route('/admin/shutdown', methods=['GET', 'POST'])
@admin_required
def shutdown():
    '''
    A most dangerous route with limited practical purpose. Accessing this
    URL as the admin will shutdown your server, remotely.
    '''
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'
    