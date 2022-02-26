import cv2
import pytesseract


class TextDetector():
    def __init__(self, img_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Programs\\Tesseract-OCR\\tesseract.exe'
        self.img = cv2.imread(img_path)

    def find_text(self):
        return pytesseract.image_to_string(self.img, lang="eng")
