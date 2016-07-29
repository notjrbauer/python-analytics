import logging
import analytics
import dateutil.parser

from pprint import pprint
from datetime import datetime
from flask import Flask, request, json

analytics.write_key = 'i6aoC3CdUjS4BvSOvmJQguLBAlvzt6kG'
analytics.debug = True

app = Flask(__name__)

def format_response (event_name):
    return json.dumps({'message': 'Successs', 'event': event_name})

def format_timestamp (timestamp):
    if timestamp is None:
        timestamp = str(datetime.now())
    return dateutil.parser.parse(timestamp)

@app.route("/identify", methods=['POST'])
def identify():
    try:
        content = request.get_json(silent=True)
        _userId = content.get('userId')
        _traits = content.get('traits')
        _context = content.get('context')
        _timestamp = format_timestamp(content.get('timestamp'))
        _anonymous_id = content.get('anonymousId')
        _integrations = content.get('integrations')

        res = analytics.identify(_userId, _traits, _context, _timestamp, _anonymous_id, _integrations)
        return format_response('identify')
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route("/alias", methods=['POST'])
def alias():
    try:
        content = request.get_json(silent=True)
        _previous_id = content.get('previousId')
        _userId = content.get('userId')
        _context = content.get('context')
        _timestamp = format_timestamp(content.get('timestamp'))
        _integrations = content.get('integrations')

        analytics.alias(_previous_id, _userId, _context, _timestamp, _integrations)

        return format_response('alias')
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route("/page", methods=['POST'])
def page():
    try:
        content = request.get_json(silent=True)
        _userId = content.get('userId')
        _event = content.get('event')
        _category = content.get('category')
        _name = content.get('name')
        _properties = content.get('properties')
        _context = content.get('context')
        _timestamp = format_timestamp(content.get('timestamp'))
        _anonymous_id = content.get('anonymousId')
        _integrations = content.get('integrations')

        analytics.page(_userId, _category, _name, _properties, _context, _timestamp, _anonymous_id, _integrations)

        return format_response('page')
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route("/track", methods=['POST'])
def track():
    try:
        content = request.get_json(silent=True)
        _userId = content.get('userId')
        _event = content.get('event')
        _properties = content.get('properties')
        _context = content.get('context')
        _timestamp = format_timestamp(content.get('timestamp'))
        _anonymous_id = content.get('anonymousId')
        _integrations = content.get('integrations')

        analytics.flush()
        analytics.track(_userId, _event, _properties, _context, _timestamp, _anonymous_id, _integrations)

        return format_response('track')

    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route("/group", methods=['POST'])
def group():

    try:
        content = request.get_json(silent=True)
        _userId = content.get('userId')
        _groupId = content.get('groupId')
        _traits = content.get('traits')
        _context = content.get('context')
        _timestamp = format_timestamp(content.get('timestamp'))
        _anonymous_id = content.get('anonymousId')
        _integrations = content.get('integrations')

        analytics.flush()
        analytics.group(_userId, _groupId, _traits, _context, _timestamp, _anonymous_id, _integrations)

        return format_response('group')

    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
