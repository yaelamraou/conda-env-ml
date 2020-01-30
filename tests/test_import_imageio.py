#!/usr/bin/env python

import unittest


class SmokeTestImageio(unittest.TestCase):
    def test_import_imageio(self):
        import imageio


if __name__ == "__main__":
    unittest.main()
