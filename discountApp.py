# Step 1: Define the function using def
# Step 2: Use an if statement to check if the discount percentage is 20% or higher
# Step 3: If the condition is met, calculate the discounted price and return it
# Step 4: If the condition is not met, return the original price

def calculate_discount(price, discount_percent):
    #This is where I will check the discount for 20% or higher
    if discount_percent >= 20:
        final_price = (price * discount_percent / 100)
        return final_price
    else:
        return price
    

# Step 5: Prompt the user for input using input()
# Step 6: Convert the input strings to float using float() or int() as needed
# Step 7: Call the calculate_discount function with the user-provided values
# Step 8: Print the result to the user

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print("The final price after discount is:", final_price)