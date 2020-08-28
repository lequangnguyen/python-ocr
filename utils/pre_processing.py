import cv2


def upgrade_image(image):
    """Do pre_processing image before the action of Tesseract-OCR."""
    # load the image and convert it to grayscale
    image = cv2.imread(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
