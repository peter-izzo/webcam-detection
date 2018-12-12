import cv2

face_cascade=cv2.CascadeClassifier("C:\\Users\\Pete\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\cv2\\haarcascade_frontalface_default.xml")

img=cv2.imread("C:\\Users\\Pete\\AppData\\Local\\Programs\\Python\\Python36-32\\Projects\\cv2\\shrek.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.01,
minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),3)

print(type(faces))
print(faces)

resized=cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("updated",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
