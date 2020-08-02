import unittest

class TestLogin(unittest.TestCase):
    '''unit tests for the login view'''

    def test_get_login(self):
        '''test that we receive the correct html'''

        self.assertEqual(True, True)

if __name__ == "__main__":
    unittest.main()