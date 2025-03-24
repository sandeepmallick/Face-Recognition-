import cv2
# Load the pre-trained model
a=cv2.CascadeClassifier("C:/Users/sande/OneDrive/Documents/Desktop/snake/PROJECT/FACE/haarcascade_frontalface_default.xml")
b=cv2.VideoCapture(0)

# it Start loop to capture frames from camera
while True:
    rectangle,image=b.read()
    c=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    d=a.detectMultiScale(c,1.3,7)
    
# Loop to detecte all faces
    for (x,y,w,h) in d:
        
# Draw a rectangle around the faces      
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),5)
# show the live video      
        cv2.imshow("image_live",image)
        # ord ("a") is used to break the loop
        if cv2.waitKey(10)==ord("a"):
            break
b.release()
cv2.destroyAllWindows()
