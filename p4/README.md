#### start:	
#### finish:

### Largest palindrome product 

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


### Notes

- The problem statement mentions that the largest number should be made from the product of the two 3 digits numbers.
- It means that the largest palindrome should have 2 factors both of 3 digits.
- From this the domain of the numbers where this number will be the product of the 3 digits numbers.
	A = {n : n ∈ ℕ, 100*100 ⩽ n ⩽ 999*999} 
	Largest Palindrome of 3 Digits ∈ {10000, 10001,...,998001}

- Iterative approach will be to start from the end and check for the palindrome propoerty of every number and move.
- Need to write the function to check if an number is palindrome or not.



#### What is Palindrome
- Numbers or Letter sequence which are same if read from the reverse direction.
- All single digit number are palindrome. 0,1,2,3,4,5,6,7,8,9
- All two digits number which are palindrome are also divisible by 11
	11,22,33,44,55,66,77,88,99
- All three digit palindrome:
	- assume three digit number - abc
	- for its to be palindrome - a == b, and these can be any among {1...9} - 9 options
	- c can be any from {0...9}, 10 options.
	- So this makes it 90 Palindrome Numbers which are of three digits.

- All 4 digit numbers 
	- assume a four digit number - abcd
	- a == c, {1...9}, 9 options.
	- b == c, {0...9}, 10 options. If they are not equal then the number will not be same from 		reverse.
	- So this makes it 90 Palindromes

- Extrapolating this can be used to find more numbers which are palindrome.

- All 5 digit numbers
	- assume a 5 digit number - abcde
	- a == e, {1...9}, 9 options.
	- b == d. {0...9}, 10 options.
	- c can be any from {0...9}, 10 options.
	- So this makes it 900 Palindrome Numbers of 5 digit.




