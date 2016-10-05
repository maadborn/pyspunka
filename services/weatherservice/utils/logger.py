'''logger'''

import datetime
import sys

def log_error(message, exception):
    '''log_error'''
    print(
        '{} {} {}'.format(datetime.datetime.now(), message, str(exception)),
        file=sys.stderr,
        flush=True)

def log_info(message):
    '''log_info'''
    print(
        '{} {}'.format(datetime.datetime.now(), message),
        file=sys.stdout,
        flush=True)
