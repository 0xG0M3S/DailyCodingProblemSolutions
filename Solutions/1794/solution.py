
a = int(input("First heap: "))
b = int(input("Second heap: "))
c = int(input("Third heap: "))

xor = (a ^ b) ^ c

if(xor > 0):
    print(f"First player will win. ({xor})")
else:
    print(f"Second player will win ({xor})")