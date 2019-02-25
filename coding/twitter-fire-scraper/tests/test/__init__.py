"""
This is a suite of test tests, meant to be run on various quantifiable parts of this project to ensure they work as
intended.
"""
import os
import sys
import unittest

# Append parent directory to enhance portability.
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

if __name__ == "__main__":
    loader = unittest.TestLoader()

    # Load current directory
    suite = loader.discover("./")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)