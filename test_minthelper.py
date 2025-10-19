# test_minthelper.py
"""
Tests for MintHelper module.
"""

import unittest
from minthelper import MintHelper

class TestMintHelper(unittest.TestCase):
    """Test cases for MintHelper class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintHelper()
        self.assertIsInstance(instance, MintHelper)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintHelper()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
