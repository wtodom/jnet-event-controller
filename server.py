import sys
import json

from flask import Flask, request


app = Flask(__name__)


@app.route('/receive', methods=['POST'])
def receive():
    with open('request.log', 'w+') as f:
        request_json = json.loads(request.data.decode('utf8'))
        print('Message from jnet-notifier-extension: ' + request_json['msg'], file=sys.stderr)
        if 'steal' in request_json['msg']:
            print('\n\t~~~ ALERT!ALERT!ALERT! ~~~\n\tHit that air horn, we rekkin\'!\n', file=sys.stderr)
    return 'Success'