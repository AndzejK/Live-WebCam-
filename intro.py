import cv2
from flask import Flask,render_template, Response
video=cv2.VideoCapture(0) # access the cammera 0 or 1
# generator
def get_frame():
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
    return Response(get_frame, mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
