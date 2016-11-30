import unittest
from app.logic import *

class TestCalculator(unittest.TestCase):
	#Tests that our function adds correctly
	def test_magic_sum(self):
		self.assertEqual(magic_sum(5),15)
     
          #tests that our function divides correctly
	def test_magic_div(self):
		self.assertEqual(magic_div(5),2)

	def test_magic_multipy(self):
		#tests that our function multipliies correctly
		self.assertEqual(magic_multiply(10),100)

	def test_magic_array(self):
		#an array is returned
		return magic_array(100)

	def test_even(self):
		#tests even numbers
		return magic_even(100)

	def test_generate_primes(self):
		#generates prime numbers
	    return generate_prime_numbers(100)

if __name__ == '__main__':
	unittest.main()