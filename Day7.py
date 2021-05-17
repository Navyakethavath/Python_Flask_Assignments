#Give all the index values of vowels.

li=['a','e','i','o','u']
word="navya"
for i in range(len(word)):
   if word[i] in li:
       print (i)

#Reverse the words of a string
s = "Hello world"
print(s[::-1])

#Remove duplicate elemnts without using set()
li = [1,2,3,3,2,4]
li.remove(3)
del li[3]
print(li)
