#Count the lower-case vowels in an input string

vowel_count = 0
vowel_list = 'aeiou'

my_string = input("Enter an input string, enter <enter> to quit: ")
my_string = my_string.lower()
for a_char in my_string:
    if a_char in my_string:
        vowel_count +=1
print(f'vowel count = {vowel_count}')

