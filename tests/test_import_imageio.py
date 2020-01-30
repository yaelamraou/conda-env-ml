#!/usr/bin/env python

import unittest


class SmokeTestImageio(unittest.TestCase):
    """
    imageio smoke tests.

    Args:
        unittest (unittest.TestCase): unittest base class.

    """

    @staticmethod
    def test_import_imageio():
        """Test: import imageio."""
        import imageio

        print(imageio.__version__)


if __name__ == "__main__":
    unittest.main()
