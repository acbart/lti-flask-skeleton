import os

# Flask tools
from flask import send_from_directory, url_for

# Application specific
from main import app
from models.models import db, User, Role

@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    '''
    Manually provide the favicon from the static folder.
    '''
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/site-map", methods=['GET', 'POST'])
def site_map():
    '''
    Useful snippet for providing a complete map of your site.
    '''
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        try:
            url = url_for(rule.endpoint, **options)
        except:
            url = "Unknown error"
        line = urllib.unquote("<td>{:50s}</td><td>{:20s}</td><td>{}</td>".format(rule.endpoint, methods, url))
        output.append(line)
    return "<table><tr>{}</tr></table>".format("</tr><tr>".join(sorted(output)))
        