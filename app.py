def check_divisible(arr):
    for number in arr:
        if ((number % 3 == 0) & (number % 5 == 0)):
            print("FizzBuzz", number)
        elif (number % 3 == 0):
            print("Fizz", number)
        elif (number % 5 == 0):
            print("Buzz", number)
        else:
            print("None divisible", number)

numbers = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

print(check_divisible(numbers))