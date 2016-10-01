import datetime
import sys
from pprint import pprint

def log_error(message, exception):
    print('{} {} {}'.format(datetime.datetime.now(), message, str(exception)), file=sys.stderr, flush=True)
    
def log_info(message):
    print('{} {}'.format(datetime.datetime.now(), message), file=sys.stdout, flush=True)