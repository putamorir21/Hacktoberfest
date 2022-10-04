def bruteforce_cal(stock,count):
    if (count >= len(stock)):
        return 0
    maxcount = 0
    for i in range(count, len(stock)):
        maxprofit = 0
        for j in range(i+1, len(stock)):
            if (stock[i] < stock[j]):
                profit = bruteforce_cal(stock, j + 1) + stock[j] - stock[i]
                if (profit > maxprofit):
                    maxprofit = profit
                
        if (maxprofit > maxcount):
            maxcount = maxprofit
        
    return maxcount
    
    
