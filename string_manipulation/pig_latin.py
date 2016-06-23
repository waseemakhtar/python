'''
   pig latin is the output for the given word which moves the
   starting alphabet of the word to the end and appends 'ay'
   at the end.
   For example, if the word is 'hello', the pig latin output
   is 'ellohay'
'''
input_letter = input("Enter the string:")

#return the letter at the location 0
first_letter = input_letter[0]

#return the size/length of the inputted string
length = len(input_letter)

#return the size/length of the inputted string
length = len(input_letter)

#'+' operation with strings resultin concatination
input_letter = input_letter[1:]+first_letter+'ay'

print(input_letter)
