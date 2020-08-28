def validate_input_file_extension(file_name):
    """Validate input file extension."""
    ext = '.png', '.jpg', '.jpeg', '.pdf'
    return file_name.endswith(ext)


def validate_output_file_extension(file_name):
    """Validate output file extension."""
    ext = '.txt', '.text'
    return file_name.endswith(ext)