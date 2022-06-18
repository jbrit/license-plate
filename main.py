from text import get_text
from crop import crop_black_quadrilateral


cropped_loc = crop_black_quadrilateral(input("Enter the path of the image: "))
print(cropped_loc)
if cropped_loc:
    print(get_text(cropped_loc))
else:
    print('No license plate found')