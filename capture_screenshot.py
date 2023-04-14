from mss import mss
from datetime import datetime
import time

structure_for_date_and_time="%Y-%m-%d_%H:%M:%S"

while True:
    current_time=datetime.utcnow() 
    current_time_str=current_time.strftime(structure_for_date_and_time)
    with mss() as screen:
        file_name=f'screenshots/scrshot_{current_time_str}.png'
        screen.shot(output=f'screenshots/scrshot_{current_time_str}.png')
        print(file_name)
    time.sleep(60)