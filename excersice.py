#1.Write a Python function to find the maximun of three numbers
'''''
num1=3
num2=6
num3=9

def max_of_three(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(f'The biggest number is {max_of_three(num1,num2,num3)}')


#2. Write a Python function to sum all the numbers in a list

my_list=[7,5,3,1]

def sum_list_num(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
result = sum_list_num(my_list)
print(f'The sum of the numbers in my list is {result}')


#3. Write a Python function to muliply all the numbers in a list

my_list = [2,5,8, -9]

def sum_list_numb(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total 
result = sum_list_numb(my_list)
print(f'The product of the numbers in my list is {result}')


#4. Write a Python program to reverse a string.

astring= input("Enter a string to reverse: ")
def my_function(txt):
    return txt[::-1]
mytxt = my_function(astring)

print(mytxt)


#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

n=int(input("Enter a number: "))

def cal_factor(n):
   
    if n==0:
        return 1
    else:
        return n * cal_factor(n-1)
    
result = cal_factor(n)
print(f'The factorial of {n} is: {result}')



#6. Write a Python function to check whether a number falls within a given range.

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
num_to_check = int(input("Enter the number to check: "))

def is_in_range(number, start, end):
    return start <= number <= end

if is_in_range(num_to_check, start_range, end_range):
    print(f'{num_to_check} is within the range {start_range} to {end_range}')
else:
    print(f'{num_to_check} is not within the range {start_range} to {end_range}')



#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.

user_input= input("Enter any string: ")

def any_string(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count +=1

        elif char.islower():
            lower_count +=1

    return upper_count, lower_count

upper_count, lower_count = any_string(user_input)

print("Uppercase letters: ", upper_count)
print("Lowercase letters: ", lower_count)
'''''

#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

input_list = [1,2,3,3,3,4,4,5,5,5,5,5]

x =[]
for a in input_list:
    if a not in x:
        x.append(a)

print(x)


#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def prime(num):

    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2,num):
            if(num % x ==0):
                return False
        return True
            
while True:
    user_input = int(input("Enter a number: "))
    if prime(user_input):
        print(f"{user_input} is a prime number.")
        break  # Exits the loop if a prime number is entered
    else:
        print(f"{user_input} is not a prime number. Please try again.")


