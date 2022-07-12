import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract'
def get_text(file_path):
    value = pytesseract.image_to_string(file_path, config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8', lang='eng')
    def charToNumber(char: str):
        char_dict = {
                "0": "O",
                "1": "I",
                "3": "B",
                "4": "A",
                "5": "S",
                "6": "G",
                "7": "Z",
                "8": "B",
        }
        return char_dict.get(char, char)
    if len(value) < 4:
        raise Exception("Could not generate a valid plate number")
    if len(set(value)&set("0123456789")) == 0:
        return ""
    value = value.strip()
    return charToNumber(value[0]) + charToNumber(value[1]) + value[2:-2] + charToNumber(value[-2]) + charToNumber(value[-1]) 