import cv2
import numpy as np

def crop_black_quadrilateral(img: np.ndarray[int, np.dtype[np.generic]]):
    # img = cv2.resize(img, (300, 300))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    cv2.imshow("edged", edged)
    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = img.copy()
    cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
    cv2.imshow("contours", image1)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    screenCnt = None
    image2 = img.copy()
    cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
    cv2.imshow("Top 30 contours", image2)
    # cv2.waitKey(0)
    i = 7
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(c)
            new_img = img[y:y + h, x:x + w]
            new_path = './' + str(i) + '.jpg'
            # cv2.imwrite(new_path, new_img)
            return new_img
        i += 1
