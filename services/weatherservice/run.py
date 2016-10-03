'''run'''

import sys
from wsmain.weatherservice import WeatherService

def start_service():
    '''start_service'''
    wsservice = WeatherService()
    try:
        wsservice.start()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n', file=sys.stderr, flush=True)
        sys.exit(0)

if __name__ == '__main__':
    start_service()
