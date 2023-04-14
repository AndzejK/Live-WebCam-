from mss import mss
with mss() as screen:
    screen.shot(output='screenshots/scrshot_v2.png')