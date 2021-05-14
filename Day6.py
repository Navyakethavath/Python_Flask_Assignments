#Count even numbers and odd numbers

list1 = [21,3,4,6,33,2,3,1,3,76]
even_count, odd_count = 0, 0
for num in list1:
   if num % 2 == 0:
      even_count += 1
   else:
      odd_count += 1
print("Even numbers available in the list: ", even_count)
print("Odd numbers available in the list: ", odd_count)


#Tell max and min of the list ( without using any inbuilt function like max(),min())
NumList = []
Number = int(input("How many element in list, please enter num :- "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList.append(value)
NumList.sort()
print("The Minimum value of the List is : ", NumList[0])
print("The Maximum value of the List is : ", NumList[Number - 1])


#Check whether the whole list is palindrome or not
test_list = [1, 4, 5,4, 1]
print("The original list is : " + str(test_list))
reverse = test_list[::-1]
res = test_list == reverse
print("Is list Palindrome : " + str(res))

