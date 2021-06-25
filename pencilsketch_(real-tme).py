import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, webcam = cap.read()

    webcam_gray = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)
    webcam_gray_inv = cv2.bitwise_not(webcam_gray)
    webcam_gray_inv_blur = cv2.GaussianBlur(webcam_gray_inv, ksize=(21, 21), sigmaX=None, sigmaY=None)

    webcam_divide = cv2.divide(webcam_gray, 255 - webcam_gray_inv_blur, scale=256)

    cv2.imshow("sketching", webcam_divide)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()