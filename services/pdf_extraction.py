import pytesseract
import os
from pdf2image import convert_from_path
from services import img_extraction
from utils import output_optimization
from configparser import ConfigParser
from utils import logger as logger_util


def extract_from_pdf(input_file, output_file, verbose):
    """Extracting text from a pdf file and save it to output folder."""
    config_object = ConfigParser()
    config_object.read("config.ini")
    tool_path = config_object['TOOL_PATH']
    tesseract_path = tool_path['tesseract']
    poppler_path = tool_path['poppler']

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    logger = logger_util.get_logger(verbose, __name__)
    try:
        pages = convert_from_path(input_file, "ddfsf", poppler_path=poppler_path)

        image_counter = 1
        for page in pages:
            # Declaring filename for each page of PDF as JPG
            # For each page, filename will be:
            # PDF page 1 -> page_1.jpg
            # PDF page 2 -> page_2.jpg
            # PDF page 3 -> page_3.jpg
            # ....
            # PDF page n -> page_n.jpg
            filename = "page_" + str(image_counter) + ".jpg"

            # Save the image of the page in system
            page.save(filename, 'JPEG')

            # Increment the counter to update filename
            image_counter = image_counter + 1
            filelimit = image_counter - 1

            # Open the file in append mode so that
            # All contents of all images are added to the same file
            f = open("output_files/" + output_file, "a")

            # Iterate from 1 to total number of pages
            for i in range(1, filelimit + 1):
                # Set filename to recognize text from
                # Again, these files will be:
                # page_1.jpg
                # page_2.jpg
                # ....
                # page_n.jpg
                filename = "page_" + str(i) + ".jpg"
                text = img_extraction.extract_text_from_img(filename, verbose)
                text = output_optimization.optimize(text)
                # Finally, write the processed text to the file.
                f.write(text)
                # Remove file
                os.remove(filename)
                # Close the file after writing all the text.
            f.close()
            return True

    except Exception as e:
        logger.error(e)
        f.close()
        os.remove(output_file)
        return False
