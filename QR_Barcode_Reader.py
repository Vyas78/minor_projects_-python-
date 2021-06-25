import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    code=decode(img)
    for barcode in decode(img):
        qrdata = barcode.data.decode('utf-8')  # width and height
        print(qrdata)
        qrsize = barcode.rect
        print(qrsize)

        # put a polygon on the barcode
        polygon = np.array([barcode.polygon], np.int32)
        polygon = polygon.reshape((-1, 1, 2))
        cv2.polylines(img, [polygon], True, (255, 0, 255), 3)
        # putting text
        cv2.putText(img, qrdata, (qrsize[0], qrsize[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    cv2.imshow("scanning", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

