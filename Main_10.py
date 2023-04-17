# More about cv2
# Opening your webcam

import cv2

camera = cv2.VideoCapture(0)

while True:
    ret , frame = camera.read()
    cv2.imshow("Press spacebar to exit frame",frame )

    if cv2.waitKey(1) & 0xff == ord(' '):
        break

camera.release()
camera.destroyAllWindows()