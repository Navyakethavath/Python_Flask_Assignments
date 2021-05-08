#From range n to m, print all the numbers divisible by 5 and 7 both

M=5
N=7
print ("Numbers divisible by {0} and {1}".format (M, N))
for num in range(1,100):
	if( num%M==0 and num%N==0 ) :
		print (num)


# 2 +22 + 222 + 2222 + .. n terms

num = 5
res = 0
st = '2'
for i in range(1, num+1):
    a = int(st * i)
    res += a
print(res)


#Write a loop to find the factorial of any number

factorialnum = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#code to get P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e expected output

st = 'python language is best programming language'
for i in range(len(st)):
    end_value = '-'

    if st[i] == ' ' or i == len(st)-1 or st[i+1] == ' ':
        end_value = ''

    if i%2 == 0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i].lower(), end=end_value)

