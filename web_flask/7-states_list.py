#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''The states_list page.'''
    comp_states = list(storage.all(State).values())
    comp_states.sort(key=lambda x: x.name)
    ctxt = {
        'states': comp_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
