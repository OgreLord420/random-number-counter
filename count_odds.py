# Add the odd numbers between 0 and 5000

# setup
result = 0

# work1
# let's look at the numbers form 0 to 5000
num = 0
while num <= 5000:
    is_odd = num % 2 != 0
    if is_odd:
       result += num
    num += 1







print(result)