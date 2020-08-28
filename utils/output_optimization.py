def optimize(text):
    """Optimize text after extracting from tesseract-OCR."""
    text = text.replace('-\n', '')
    return text
