import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, webcam = cap.read()

    # converting the BGR image to GRAYSCALE
    webcam_gray = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)

    # Inverting the image
    webcam_gray_inv = cv2.bitwise_not(webcam_gray)

    # Applying Gaussian Blur to the inverted image
    webcam_gray_inv_blur = cv2.GaussianBlur(webcam_gray_inv, ksize=(21, 21), sigmaX=None, sigmaY=None)

    # Dividing the GRAYSCALE image by blurred inverted GRAYSCALE image
    webcam_divide = cv2.divide(webcam_gray, 255 - webcam_gray_inv_blur, scale=256)

    cv2.imshow("sketching", webcam_divide)

    # Exiting the image window by pressing button q on keyboard
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()