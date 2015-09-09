def factorial(number_for_factorial):
	prod = 1
	while(number_for_factorial!=1):
		prod *= number_for_factorial
	return prod


def gcd(number_1, number_2):
    if(number1<number2):
		number1,number2 = number2,number1
	while(number2!=0):
		number_1,number_2 = number_2,number_1%number_2
    return number_1


def is_palindrome(string_to_check):	
	new_string = string_to_check[::-1]
	if new_string == string_to_check:
		return True
	return False


#Take input for fib in variable a

print(fib(a))


#Take input for is_prime in variable b, c

print(gcd(b, c))


#Take input for is_palindrome in variable d

print(is_palindrome(d))