# Python program to count the number of occurrence of a y in the given string
str= (input("Enter the string : "))
substring = 'y'
count = str.count(substring)
print('The substring occurs {} times'.format(count))


#take input of a string and print it's even indexed characters
str=input("enter the string:")
even_indexed_characters = str[::2]
print(even_indexed_characters)


#create a program to swap case. Using string functions
st = input("enter the string")
print(st.swapcase())
