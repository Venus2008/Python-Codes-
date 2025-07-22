def check_multiple(n):
    if n%5==0 and n%7==0 and n%10==0 and n%56==0:
        return "It is Divisible"
    else:
        return "Not Divisible"
print(check_multiple(280))

