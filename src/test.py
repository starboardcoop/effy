import unittest
from main import read_file
from main import list_people


class YamlReaderTests(unittest.TestCase):

    def test_read_file(self):
        data = read_file()
        self.assertIn('standings', data)
    
    def test_list_people(self):
        data = read_file()
        list_people(data)


if __name__ == '__main__':
    unittest.main()