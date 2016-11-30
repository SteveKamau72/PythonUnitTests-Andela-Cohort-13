import unittest
from app.logic import *

class TestCalculator(unittest.TestCase):
	#Tests that our function adds correctly
	def test_magic_sum(self):
		self.assertEqual(magic_sum(5),15)
       


if __name__ == '__main__':
	unittest.main()