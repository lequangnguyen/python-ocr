import unittest
import os
from utils import path_checker
from utils import extension_validation

resources_input_directory = "tests/resources/input_files/"
resources_output_directory = "tests/resources/output_files/"
input_file = "image_test.jpg"
output_file = "image_test.txt"


class Testing(unittest.TestCase):
    def test_check_input_file_path_true(self):
        existing_file_input_path = resources_input_directory + input_file
        self.assertTrue(path_checker.check_file_path(existing_file_input_path))

    def test_check_file_output_path_true(self):
        existing_file_input_path = resources_output_directory + output_file
        self.assertTrue(path_checker.check_file_path(existing_file_input_path))

    def test_input_file_extension(self):
        self.assertTrue(extension_validation.validate_input_file_extension(input_file))

    def test_output_file_extension(self):
        self.assertTrue(extension_validation.validate_output_file_extension(output_file))


if __name__ == '__main__':
    unittest.main()
