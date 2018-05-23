

num = 17

if num > 1:   #prime nubers are greater than one
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"it is not prime num")
       print(i,"times",num//i, "is",num)
       break
   else:
      print (num,"is a prime number")

else:
    print(num,"is is not prime number")