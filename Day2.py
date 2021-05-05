# Take variables with values of different types #

name = 'Navya'
print(name)
age = 19
print(age)
score = 95.4
print(score)
unmarried = True
print(unmarried)


#Print these in different lines and with appropriate messages (use .format()) #

name = 'Navya'
value= ' learn python'
print('I am ' + name +'.'+ 'I feel glad to '+value +' here'+'.')


# Practice Type conversion functions (str(), int(), float() , bool() etc) #

name = 'Navya'
print(type(name), name)
name = bool(name)
print(type(name), name)

name = int(name)  #int and float conversions gives errors for a string #
print(type(name), name)
name = float(name)
print(type(name), name)



age = 10
print(type(age), age)
age = str(age)
print(type(age), age)
age = float(age)
print(type(age), age)
age = bool(age)
print(type(age), age)


score = 95.4
print(type(score), score)
score = int(score)
print(type(score), score)
score = bool(score)
print(type(score), score)
score = str(score)
print(type(score), score)


unmarried = True
print(type(unmarried), unmarried)
unmarried = str(unmarried)
print(type(unmarried), unmarried)

unmarried = int(unmarried))   # we find errors in this coversion of  bool to int and float #
print(type(unmarried), unmarried)
unmarried = float(unmarried)
print(type(unmarried), unmarried)
