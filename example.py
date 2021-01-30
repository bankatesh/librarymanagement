num = int(input("enter no."))
a = len(str(num))
sum = 0
b = num

while b >0:
    d  = b%10
    sum += d**a
    b //= 10
    if num == sum:
        print("this is armstrong no.")


