import unittest
from main import read_file
from main import OrgData


class YamlReaderTests(unittest.TestCase):

    def test_read_file(self):
        data = read_file()
        self.assertEqual(3, len(data.people))
        self.assertEqual(3, len(data.standings))


if __name__ == '__main__':
    unittest.main()