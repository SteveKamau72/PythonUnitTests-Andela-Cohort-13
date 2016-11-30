import unittest
from app.logic import *

class TestCalculator(unittest.TestCase):
	#Tests that our function adds correctly
	def test_magic_sum(self):
		self.assertEqual(magic_sum(5),15)
     
          #tests that our function divides correctly
	def test_magic_div(self):
		self.assertEqual(magic_div(5),2)


if __name__ == '__main__':
	unittest.main()