from __future__ import print_function
import cv2 as cv
import argparse

def detectAndDisplay(frame): # 얼굴을 감지하고 화면에 표시한다
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #색상 전환
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        faceROI = frame[y:y+h,x:x+w]
        # frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,0), -1)
        # faceROI를 모자이크처리
        faceROI = cv.GaussianBlur(faceROI, (0, 0), 20)
        frame[y:y+h,x:x+w] = faceROI
    
    cv.imshow('Capture - Face detection', frame)


parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='./haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='./haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break