def fib_sum_even() -> int:
    dp = list()
    # adding values for dp[0] and dp[1]
    dp.append(0)
    dp.append(1)
    
    sum  = 0
    
    while dp[-1] < 4000000:
        dp.append(dp[-1] + dp[-2])
        
        # checking if value is even
        if dp[-1] % 2 == 0:
            sum += dp[-1]
        
    return sum

print(fib_sum_even())
        