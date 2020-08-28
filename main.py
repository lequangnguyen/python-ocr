import os
from os import path

import click

from services import img_extraction, pdf_extraction
from utils import extension_validation
from utils import logger as logger_util
from utils import constants


@click.command()
@click.option('--input', required=True, help='file input path')
@click.option('--output', required=True, help='file output path')
@click.option('--verbose', is_flag=True, help='output detailed logs')
def main(input, output, verbose):
    """main is the request handling function."""
    # Get logger
    logger = logger_util.get_logger(verbose, __name__)
    # Do input validation
    input_exist = path.exists(input)

    if not input_exist:
        logger.error("input file name is not exist!")
        return 1

    output_exist = path.exists(constants.OUTPUT_DESTINATION + output)

    if output_exist:
        logger.error(output +
                     " file existed! Please choose another name for output")
        return 1

    input_file_extension_check = extension_validation.validate_input_file_extension(
        input)

    if not input_file_extension_check:
        logger.error(
            "Wrong input file extension! Only accept extensions including jpg, jpeg, png, pdf!"
        )
        return 1

    output_file_extension_check = extension_validation.validate_output_file_extension(
        output)

    if not output_file_extension_check:
        logger.error("Output file extension should be txt or text!")
        return 1

    # Start processing for extraction
    file_extension = os.path.splitext(input)

    logger.info("Starting extract text from input file")
    logger.info("Processing......")
    if file_extension[1] == '.pdf':
        result_check = pdf_extraction.extract_from_pdf(input, output, verbose)
    else:
        result_check = img_extraction.extract_from_image(input, output, verbose)
    if result_check:
        logger.info("Finish! Result is saved to tha path of " + constants.OUTPUT_DESTINATION +
                output)


if __name__ == '__main__':
    main()
