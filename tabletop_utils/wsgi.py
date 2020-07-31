'''
entry point for wsgi server
'''

import signal
import sys

from tabletop_utils import create_app

def signal_handler(sig, frame):
    '''SIGINT received, killing the service.'''

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

app = create_app()

if __name__ == "__main__":
    app.run()
