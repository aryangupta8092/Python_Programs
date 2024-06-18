#M1 Slice method
a = input("Enter the value:")
reverse = a [::-1]
if(a== reverse):
    print("Yes,it is palindrome")
else:
    print("No, it is not palindrome")

#................................................
#M2
num = int(input("Enter the number"))  # Take an integer input from the user and store it in num
temp = num  # Store the original value of num in temp (currently not used further)
reverse = 0  # Initialize reverse to 0

# Loop to reverse the digits of the number
while num > 0:
    dig = num % 10  # Get the last digit of num
    reverse = reverse * 10 + dig  # Add the digit to the reverse number in the correct position
    num = num // 10  # Remove the last digit from num

print(reverse)  # Print the reversed number


#print(type(num)) if we write num = input() i.e string

#...............................................