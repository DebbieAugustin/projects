number = ""
while(not(number.isnumeric())):
    number= input("What is the decimal to convert? ")
tempnumb = int(number)
bin_output= ""
while(tempnumb>0):
    bin_output= str(tempnumb % 8) + bin_output
    tempnumb= int(tempnumb/8)
print(bin_output)