import sys
import json

from flask import Flask, request


app = Flask(__name__)


class MessageTypes:
    START_PSI_GAME = "START_PSI_GAME"
    INITIATE_A_TRACE = "INITIATE_A_TRACE"
    GAIN_A_CREDIT = "GAIN_A_CREDIT"
    DRAW_A_CARD = "DRAW_A_CARD"
    CONCESSION = "CONCESSION"
    PURGE_ALL_VIRUSES = "PURGE_ALL_VIRUSES"
    AGENDA_SCORE = "AGENDA_SCORE"

    @staticmethod
    def get_message_type(msg):
        if "to start a psi game" in msg:
            return MessageTypes.START_PSI_GAME
        elif "to initiate a trace with strength" in msg:
            return MessageTypes.INITIATE_A_TRACE
        elif "spends [Click] to gain 1 [Credits]" in msg:
            return MessageTypes.GAIN_A_CREDIT
        elif "spends [Click] to draw a card" in msg:
            return MessageTypes.DRAW_A_CARD
        elif "concedes" in msg:
            return MessageTypes.CONCESSION
        elif "all virus counters" in msg:
            return MessageTypes.PURGE_ALL_VIRUSES
        elif "scores" in msg and "and gains" in msg and "agenda point" in msg:
            return MessageTypes.AGENDA_SCORE


@app.route('/receive', methods=['POST'])
def receive():
    request_json = json.loads(request.data.decode('utf8'))
    print('Message from jnet-notifier-extension: ' +
          request_json['msg'], file=sys.stderr)
    if 'steal' in request_json['msg']:
        print(
            '\n\t~~~ ALERT!ALERT!ALERT! ~~~\n\tHit that air horn, we rekkin\'!\n', file=sys.stderr)
    return 'Success'
