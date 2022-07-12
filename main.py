import cv2
import db
from text import get_text
from crop import crop_black_quadrilateral
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def most_similar_license(license):
    most_similar = None
    high_score = 0
    for l in db.read_license():
        score = similar(l[0], license)
        if score > high_score:
            high_score = score
            most_similar = l[0]
    if most_similar is None or high_score < 0.7:
        return None
    return most_similar


def check_image(img):
    cropped_img = crop_black_quadrilateral(img)
    if cropped_img is not None:
        try:
            license_text = get_text(cropped_img).upper()
            db_text = most_similar_license(license_text)
            if db_text is None and len(license_text)>5:
                print(f"Could not find {license_text} license plate in db")
            else:
                print("The license plate was found as: " + db_text)
                print("OPEN")
        except:
            pass
    else:
        pass
        # print('No license plate found')


vidcap = cv2.VideoCapture(0)
while True:
    if vidcap.isOpened():
        ret, frame = vidcap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)
        check_image(frame)
        if(cv2.waitKey(1) ==ord("q")):
            break
    #do something
    else:
        print("Cannot open camera")