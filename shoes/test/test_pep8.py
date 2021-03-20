import unittest
import pep8

import os


def get_files(directory):
    files = []
    for f in os.listdir(directory):
        name = os.path.join(directory, f)
        if (os.path.isfile(name) and name.endswith('.py')):
            files.append(name)
        elif (os.path.isdir(name)):
            files += get_files(name)
    return files


class TestPep8(unittest.TestCase):
    def test_files(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 120
        directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        files = get_files(directory)
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0)
