num = int(input("Enter the number : \n"))  # Take an integer input from the user and store it in num
temp = num  # Store the original value of num in temp (currently not used further)
reverse = 0  # Initialize reverse to 0

# Loop to reverse the digits of the number
while num > 0:
    dig = num % 10  # Get the last digit of num
    reverse = reverse * 10 + dig  # Add the digit to the reverse number in the correct position
    num = num // 10  # Remove the last digit from num
if temp== reverse:
    print("Number is a palindrome.")
else:
    print("Number is not a palindrome.")