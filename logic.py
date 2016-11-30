def magic_sum(number):
	sum=0
	for i in range(number+1):
		sum+=i
	return sum

def magic_div(n):
	res=10/n
	return res

def magic_multiply(n):
	res=10*n
	return res

def magic_array(number):
	array=[]
	for i in range(number+1):
		array=i
	return array

def magic_even(number):
    
	for i in range(number+1):
		if number%2==0:
		  return "Number is even"
	else:
		return "Number is odd"

def generate_prime_numbers(num):
	if num>1:

	    for num in range(2,num):

		    if(num%1==0):

			    prime=False

			    if prime:

				    return num
        else:
	    return "Invalid number"

def is_string(string):
	if type (string)==type(''):
		return "Value is string"
	else:
		return "Value is not a string"
		
def calculated_array(number):
	number_array=[]
	for i in range(number):
		#if number is even
		if i%2==0:
			number_array=i/2
		else:
			number_array=i*2

	return number_array

