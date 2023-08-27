import cv2
import random
imgmain= cv2.imread("ObjectDetection1.png") #Put the main image here
img= cv2.imread("ObjectDetection2.png")  #Put the small image that you want to find inside main image here
#Small image must be exact size that it is inside main image
y1,x1,a = imgmain.shape
y2,x2,a= img.shape
a,b=0,0 #counters
resimboyut=(y2-1)*(x2-1) # to check
x2kopya=x2 #Copying so we don't lose values later
y2kopya=y2
x3=x1-x2
y3=y1-y2
y4=0
x4=0
#print(x1,y1,x2,y2,x3,y3,x2kopya,y2kopya,x4,y4,resimboyut)  # wrote while writing program to check if values are correct
#imgcizim=imgmain.copy()  # wrote to check if program is checking every pixel one by one.
#imgkucukcizim=img.copy() "Warning flashing bright images.
while True:

    #renkb=random.randint(0,251) #For 17-18. Defines random colors so it şs easier to see different pixels
    #renkg=random.randint(0,251)
    #renkr=random.randint(0,251)
    kucukx=0
    kucuky=0
    sayac=0
    for a in range(x4,x2):

        for b in range(y4,y2):
            #imgcizim[b,a]=(renkb,renkg,renkr)   #Code for line 17-18
            #imgkucukcizim[kucuky,kucukx]=(renkb,renkg,renkr)
            big=imgmain[b,a]
            smol=img[kucuky,kucukx]
            if big.all()==smol.all():
                sayac+=1


            kucuky+=1
        kucukx+=1
        kucuky=0
    if sayac>=resimboyut:
        print("FOUND!" , a , " und " , b)
        cv2.rectangle(imgmain,(a-x2kopya,b-y2kopya),(a,b),(11,0,101),1)
        cv2.imshow("resim",imgmain)
        cv2.waitKey(0)
        break

    x4+=1
    x2+=1
    if x4>=x3:
        y4+=1
        y2+=1
        x4=0
        x2=x2kopya
    if y4>=y3:
        break
    #cv2.imshow("after",imgcizim)  #Code for line 17-18
    #cv2.imshow("before",imgmain)
    #cv2.imshow("kucuk1",img)
    #cv2.imshow("kucuk2", imgkucukcizim)
    #cv2.waitKey(5)


