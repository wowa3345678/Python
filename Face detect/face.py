import cv2

filename = 'C:/Users/rudy.liu/Documents/GitHub/Python/Face detect/face.jpg'



def detect(filename):
    face_cascade = cv2.CascadeClassifier('C:/Users/rudy.liu/Documents/GitHub/Python/haarcascades/haarcascade_frontalface_alt.xml')

    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y,w, h) in faces:
        image = cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,0), 2)

    cv2.namedWindow('face detect')
    cv2.imshow('face detect', image)
    cv2.imwrite('./face_detect.jpg', image)
    cv2.waitKey(0)

detect(filename)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
