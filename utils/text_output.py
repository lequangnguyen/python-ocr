from utils import constants


def output_text(text, output_file):
    """Save output to output_files folder."""
    f = open(constants.OUTPUT_DESTINATION + output_file, "a")
    f.write(text)
    f.close()
