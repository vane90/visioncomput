import cv
import Image
cam=cv.CaptureFromCAM(0)
while True:
    im =cv.QueryFrame(cam)
    snapshot = im
    image_size = cv.GetSize(snapshot)
    cv.SaveImage("test.png",im)
    imagen=cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
    print 'imagen',imagen
    #print im
    cv.ShowImage('Camara', snapshot)
    if cv.WaitKey(30)==27:
        break
