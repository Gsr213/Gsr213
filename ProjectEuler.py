
#Method for summing a list of numbers
def sum_list(list_of_numbers):
        total = 0
        for n in list_of_numbers:
            if not check_int_or_float(n):
                print("ERROR: input is not a number!!")
                return
            total += n
        return total

#Method for checking that a variable is a number
def check_int_or_float(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return True
    return False

#Method for checking if a number is a prime number
def check_prime(n):
    i = 2
    multiples_counter = 0
    while i <= n:
        if n % i == 0:
            multiples_counter += 1
        i += 1
    
    if multiples_counter == 1:
        return True
    return False

#Method for obtaining a list of prime numbers up to the specified argument
def list_of_primes(n):
    list_of_primes = []
    i = 0
    while i <= n:
        if check_prime(i):
            list_of_primes.append(i)
        i += 1
    
    return list_of_primes


print(list_of_primes(29))


