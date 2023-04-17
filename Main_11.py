# More about cv2
# Turn you webcam eto grey scale
import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read() # reading
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Chahge to gray images
    (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 127, 255, cv2.THRESH_BINARY) # threshholding iamges
    cv2.imshow("My vid", blackAndWhiteFrame) # showing black and white
    cv2.imshow("Real vid", frame) # # showing the origiaal vid

    if cv2.waitKey(1) == 27: # Described it as 27 due to a bug
        break

capture.release()
cv2.destroyAllWindows()
