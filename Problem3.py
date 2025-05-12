
# this selution is slow - need to find a way to solve using dynamicx progroming
def find_largest_prime_number(number):
    #  checking if number is prime and if divisable by a number - calling the function on the same number
    max_list = list()
    i = number - 1
    is_prime = True
    while i > 0:
        if number % i == 0 and i != 1:
            max_list.append(find_largest_prime_number(i))
            is_prime = False
        i -= 1 
    if is_prime:
        return number
    max_list.sort(reverse=True)
    return max_list[0]


print(find_largest_prime_number(13195))                    