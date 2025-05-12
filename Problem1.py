def return_sum(number: int) -> int:
    three_itr = 3
    five_itr = 5
    sum = 0
    while three_itr < number:
        sum += three_itr
        three_itr += 3
    while five_itr < number:
        sum += five_itr
        five_itr += 5
        
    return sum


print(return_sum(1000))