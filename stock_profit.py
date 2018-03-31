#You are to write pseudo code O(n) algorithm to maximize a one day trade. 
#You will have 5 days of predicted prices and your algorithm must choose what day to buy and sell to maximize gains.  
'''
def stockmax(prices):
    dobuy=[1]*len(prices) # 1 for buy, 0 for sell
    prof=0
    m=0
    for i in reversed(range(len(prices))):
        if m<=prices[i]:
            dobuy[i]=0
            m=ai
        prof+=m-ai
    return prof  
    '''

def profits(prices):
    prices = iter(prices)
    least = next(prices)
    yield 0
    for price in prices:
        least = min(least, price)
        yield price - least

prices = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
print(max(profits(prices)))
