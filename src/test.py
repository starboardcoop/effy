import unittest
from main import read_file

class YamlReaderTests(unittest.TestCase):

    def test_read_file(self):
        contents = read_file()
        self.assertIn('standings', contents)


if __name__ == '__main__':
    unittest.main()