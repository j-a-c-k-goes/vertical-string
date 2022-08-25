'''
	verticalize the string
	use for ascii purposes
	
	• take a string as input
	• display in all capitals, vertical form
	• input: hi
	• output: 	
				- - -	H 	- - -
				- - -	I 	- - -			
'''

# process a string
def process_string(str_to_vert:str):
	for char in str_to_vert:
		# for spaces, uses bullet styling
		if char == ' ': 
			print(f'• • • {char.upper()} • • •')
		# use hypen styling
		else: 
			print(f'- - - {char.upper()} - - -')

# on run
if __name__ == '__main__':
	string_to_verticalize = str(input('type a word: '))
	processed_string = process_string(string_to_verticalize)
	processed_string