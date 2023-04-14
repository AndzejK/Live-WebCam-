import cv2
from flask import Flask,render_template, Response
video=cv2.VideoCapture(0) # access the cammera 0 or 1
# generator
def get_frame():
    while True:
        success, frame=video.read()
        sc,encoded_img=cv2.imencode('.jpg',frame)
        frame=encoded_img.tobytes()
        # here we create an image
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'+frame + b'\r\n')

# Flask instance
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/video")
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the app locally 
# if __name__=="__main__":
#     app.run(debug=True) 

# Run the app on the same network 
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0",port=33333) # My IP 192.168.0.103 
