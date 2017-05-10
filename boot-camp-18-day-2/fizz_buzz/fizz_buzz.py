def fizz_buzz(number):
    if number % 3 is 0 and number % 5 is 0:
        return "FizzBuzz"
    elif number% 3 is 0:
        return "Fizz"
    elif number % 5 is 0:
        return "Buzz"
    else:
        return number