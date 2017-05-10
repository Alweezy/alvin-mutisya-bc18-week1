def is_prime(number):
    if number is 1:
        return False
    for value in range(2, int(number ** 0.5) + 1):
        if number % value is 0:
            return False
        return True


def collect_prime_numbers(number):
    prime_numbers = []
    if isinstance(number, int):
        if number >= 2:
            prime_numbers.append(2)
        for i in range(2, number + 1):
            if is_prime(i):
                prime_numbers.append(i)
        return prime_numbers
    else:
        return 'Only integers allowed'