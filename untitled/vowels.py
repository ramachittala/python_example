
num = "2,3,4,5"

# infinite loop
while True:
   v = input("Enter a num: ")
   # condition in the middle
   if v in num:
       break
   print("That is not a vowel. Try again!")

print("Thank you!")
