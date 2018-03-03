"""
python -m unittest discover -s tests/ -p 'test_*.py'
"""
import unittest


if __name__ == '__main__':
    start_dir = '.'
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
