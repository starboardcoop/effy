import unittest
from main import OrgData


class OrgDataTests(unittest.TestCase):

    def test_OrgData_load(self):
        data = OrgData.load()
        self.assertEqual(3, len(data.people))
        self.assertEqual(3, len(data.standings))


if __name__ == '__main__':
    unittest.main()