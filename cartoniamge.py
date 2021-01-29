import cv2

cap = cv2.VideoCapture(0)

while(True):
    #kameradan okunan frame \frame which read from camera
    ret, frame = cap.read()

    #framelere filtre atılması için adımlar \steps for filter to frames
    #reading normal image
    normalscale = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #reading grayscale image
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #smoothing a grayscale frame for cartoon lines
    smoothGrayScale = cv2.medianBlur(grayscale, 5)
    #taking edges of frame
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    colorImage = cv2.bilateralFilter(normalscale, 9, 100, 100)
    #combining 2 frames
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)


    # Displaying final carton frame
    cv2.imshow('frame',cartoonImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#closing cam
cap.release()
cv2.destroyAllWindows()