import cv2

face_cascade=cv2.CascadeClassifier("C:\\Users\\ssubh\\Downloads\\haarcascade_frontalface_default.xml")

img=cv2.imread("C:\\Users\\ssubh\\Downloads\\photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,#captures the face
minNeighbors=5)


for x,y,w,h in faces:
    #rectange location and size, color, line weight
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

print(faces)#prints the area of the face
print(type(faces))
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))


cv2.imshow("Gray",gray_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()