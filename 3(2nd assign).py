import random
def check(num):
    binary = bin(num)[2:]
    print(f"Binary of {num} is {binary}")
    pos=random.randint(0,len(binary)-1)
    print(f"Random position chosen: {pos}")
    bit = binary[pos]
    print(f"Bit at position {pos}: {bit}")
    if bit == '1':
        print("Result: True")
    else:
        print("Result: False")
check(25)
check(10)