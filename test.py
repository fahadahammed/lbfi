import unittest

from src.lbfi import read_pyproject_toml


class Test_genfstab(unittest.TestCase):
    def test_read_pyproject_toml(self):
        self.assertEqual(("." in read_pyproject_toml()), True, "Should be able to read the "
                                                      "version from the pyproject.toml file.")


if __name__ == '__main__':
    unittest.main()