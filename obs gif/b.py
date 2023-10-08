import pyaudio
import numpy as np
import cv2
CHUNK = 2**10
RATE = 44100

p=pyaudio.PyAudio( )
stream=p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
              frames_per_buffer=CHUNK, input_device_index=2)

while(True):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    if int(np.average(np.abs(data)))>20:
        image = cv2.imread('1.png')
        print("입열기")
    else:
        image = cv2.imread('2.png')
        print("입닫기")
    
    cv2.imshow('image title', image)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('c'):
        cv2.destroyAllWindows()

stream.stop_stream()
stream.close()
p.terminate 
cv2.destroyAllWindows()
