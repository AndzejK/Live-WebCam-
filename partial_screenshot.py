from mss import mss,tools

with mss() as screen:
    part={'top':250,'left':900,'width':1000,'height':800}
    img=screen.grab(part)
    tools.to_png(img.rgb,img.size,output='screenshots/partial_screenshot.png')