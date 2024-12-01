
def last_number(numbers):
    last_digits = [] 
    for number in numbers:
        last_digits.append(number % 10)
    return last_digits

numbers = [123, 456, 789, 1011, 12] 
last_digits =last_number(numbers) 
print("The last digits of each number are:", last_digits)
