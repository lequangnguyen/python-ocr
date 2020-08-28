def output_text(text, output_file):
    """Save output to output_files folder."""
    f = open("output_files/" + output_file, "a")
    f.write(text)
    f.close()
