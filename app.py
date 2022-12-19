from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import model_from_json
import operator
import sys, os

app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.php')

json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
# load weights into new model
model.load_weights("model-bw.h5")
print("Loaded model from disk")

def gen():
    # Capture video frames from the device
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        _, frame = cap.read()
        # Simulating mirror image
        frame = cv2.flip(frame, 1)
        x1 = int(0.5*frame.shape[1])
        y1 = 10
        x2 = frame.shape[1]-10
        y2 = int(0.5*frame.shape[1])

        roi = frame[y1:y2, x1:x2]
    
   
     # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
        cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
        # Extracting the ROI
        roi = frame[y1:y2, x1:x2]
    
    # Resizing the ROI so it can be fed to the model for prediction
        roi = cv2.resize(roi, (64, 64)) 
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    
        result = model.predict(test_image.reshape(1, 64, 64, 1))
        prediction = {'Correctly signed A': result[0][0], 
                  'Correctly signed B': result[0][1], 
                  'Correctly signed C': result[0][2],
                  'Correctly signed D': result[0][3],
                  'Correctly signed E': result[0][4],
                  'Correctly signed F': result[0][5],
                  'Correctly signed G': result[0][6],
                  'Correctly signed H': result[0][7],
                  'Correctly signed I': result[0][8],
                  'Correctly signed J': result[0][9],
                  'Correctly signed K': result[0][10],
                  'Correctly signed L': result[0][11],
                  'Correctly signed M': result[0][12],
                  'Correctly signed N': result[0][13],
                  'Correctly signed O': result[0][14],
                  'Correctly signed P': result[0][15], 
                  'Correctly signed Q': result[0][16], 
                  'Correctly signed R': result[0][17],
                  'Correctly signed S': result[0][18],
                  'Correctly signed T': result[0][19],
                  'Correctly signed U': result[0][20],
                  'Correctly signed V': result[0][21],
                  'Correctly signed W': result[0][22],
                  'Correctly signed X': result[0][23],
                  'Correctly signed Y': result[0][24],
                  'Correctly signed Z': result[0][25]

                  }
    # Sorting based on top prediction
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    
    # Displaying the predictions
        cv2.putText(frame, prediction[0][0], (10, 120),  cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)    
        
    
        
        # Convert the frame to JPEG format
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        
        # Yield the frame to the client
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





