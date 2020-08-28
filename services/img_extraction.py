from utils import pre_processing, text_output
import pytesseract
from configparser import ConfigParser
from utils import logger as logger_util


def extract_text_from_img(input_file, verbose):
    """Extracting text from an image."""
    logger = logger_util.get_logger(verbose, __name__)
    try:
        config_object = ConfigParser()
        config_object.read("config.ini")
        tool_path = config_object['TOOL_PATH']
        pytesseract.pytesseract.tesseract_cmd = tool_path['tesseract']
        custom_config = r'-l eng --psm 6'
        img = pre_processing.upgrade_image(input_file)
        text = pytesseract.image_to_string(img, config=custom_config)
        return text

    except Exception as e:
        logger.error(e)
        return False

def extract_from_image(input_file, output_file, verbose):
    """Output a file to output_files folder."""
    text = extract_text_from_img(input_file, verbose)
    if text:
        text_output.output_text(text, output_file)
        return True
    return False
