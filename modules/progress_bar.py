import sys
import time

def show_progress(url):
    for i in range(0, 101, 10):
        sys.stdout.write(f'\r[{url}] Progress: {i}%')
        sys.stdout.flush()
        time.sleep(0.2)
    print()
