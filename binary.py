number = ""
while (not number.isnumeric()):
    number = input("What is the decimal to convert? ")
tempnumb = int(number)
octal_output = ""
while (tempnumb > 0):
    octal_digit = str(tempnumb % 8)  # Calculate the correct octal digit
    octal_output = octal_digit + octal_output
    tempnumb = int(tempnumb / 8)
print(octal_output)
