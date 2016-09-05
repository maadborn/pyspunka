import sys
import time
from weatherservice import WeatherService

if __name__ == '__main__':
    ws = WeatherService()
    try:
        ws.start()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n', file = sys.stderr, flush=True)
        sys.exit(0)