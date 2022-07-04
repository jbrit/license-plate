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
        print(most_similar, high_score)
        return None
    return most_similar

cropped_loc = crop_black_quadrilateral(input("Enter the path of the image: "))
print(cropped_loc)
if cropped_loc:
    license_text = get_text(cropped_loc).upper()
    db_text = most_similar_license(license_text)
    if db_text is None:
        print(f"Could not find {license_text} license plate in db")
    else:
        print("The license plate was found as: " + db_text)
else:
    print('No license plate found')