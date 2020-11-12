import cv2

lena = cv2.imread("lena.bmp")
cv2.imshow("demo", lena)
key = cv2.waitKey()
if key == ord("A"):
    cv2.imshow("PressA", lena)
if key == ord("B"):
    cv2.imshow("PressB", lena)
