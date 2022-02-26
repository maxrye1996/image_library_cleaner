import os
import enchant
import re
from text_detector_module import TextDetector
from textblob import Word


def handle_word(text):
    is_word = False
    words_to_check = []
    text_list = text.split("\n")
    for sentence in text_list:
        word_list = sentence.split(" ")
        words_to_check += word_list

    for target_word in words_to_check:
        target_word = target_word.lower()
        if "." in target_word:
            words = target_word.split(".")
            for word in words:
                word = re.sub('[^A-Za-z0-9]+', '', word)
                word = word.lstrip()
                if len(word) > 2:
                    word = Word(word)
                    if str(word.spellcheck()[0][1]) == "1.0":
                        is_word = True

        else:
            word = re.sub('[^A-Za-z0-9]+', '', target_word)
            word = word.lstrip()
            if len(word) > 2:
                word = Word(word)
                if str(word.spellcheck()[0][1]) == "1.0":
                    is_word = True
    return is_word


target_dir = "X:\\OneDrive - The Open University\\MergedPhotos"
output_dir = "X:\\OneDrive - The Open University\\PhotosWithText"

os.chdir(target_dir)
image_list = os.listdir()
total_images_found = len(image_list)
extension_list = ["JPG", "JPEG", "PNG"]

d = enchant.Dict("en_GB")
images_checked = 0
images_moved = 0
for img in image_list:
    text = ""
    name, extension = img.split(".")
    if extension.upper() in extension_list:
        text_detector = TextDetector(target_dir + "\\" + img)
        text = text_detector.find_text()
        if text != "":
            # print("text found:  " + text)
            is_word = handle_word(text)
            if is_word:
                os.rename(target_dir+"\\"+img, output_dir+"\\"+img)
                images_moved = images_moved + 1

    images_checked = images_checked + 1
    print("Checked " + str(images_checked) + " out of " + str(total_images_found))
    print("Moved: " + str(images_moved))

