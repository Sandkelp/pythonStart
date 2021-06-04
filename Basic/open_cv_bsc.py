
import cv2
#cv2.imwrite("newsmallgrey.png", im_g) #makes a numpy image

#im_g[0:2,2:4] #rows 0-2 and coloums from 
im_g = cv2.imread("C:\\Users\\ssubh\\Downloads\\galaxy.jpg",0) #converts the small png into the an array of grey scale values
print(im_g)
print(im_g.shape)

resized_image=cv2.resize(im_g,(int(im_g.shape[1]/2),int(im_g.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()