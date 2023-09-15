#slicing = create a sudstring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

#index[]
name = "Debbie Augustin"

first_name = name[0:3]
last_name = name[7:12]
another_name= name[0:3:2]
reverse_name = name[::-1]

print(first_name)
print(last_name)
print(another_name)
print(reverse_name)

#slice

website = "http://google.com"

slice = slice(7,-4) #reverse index

print(website[slice])