num = int(input())
rev = 0
temp = num
while
        temp > 0:
    rev = (rev*10) + (temp %10);
    temp = temp//10
    if rev == num :
        print("palindrome")
    else:
        print("not palindrome")