import cv2
def generate():
    face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('eye.xml')
    #camera = cv2.VideoCapture(0)
    camera= cv2.VideoCapture('jim.mp4',0)
    count = 0
    while (True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.5,5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            cv2.imwrite('./jm/jim_carrey/%s.png' % str(count), f)
            count += 1
        cv2.imshow("camera", frame)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
  generate()