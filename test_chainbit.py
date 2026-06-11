# test_chainbit.py
"""
Tests for ChainBit module.
"""

import unittest
from chainbit import ChainBit

class TestChainBit(unittest.TestCase):
    """Test cases for ChainBit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainBit()
        self.assertIsInstance(instance, ChainBit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainBit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
