#adding the numbers by the user input
def e_o(num):
    if(int(num) % 2 == 0):
        print("Even")
    else:
        print("Odd")
    return num;
def add(a,b):
    num = int(a) + int(b)
    return num;

n1 = input("Enter Number 1 = ")
n2 = input("Enter Number 2 = ")

print("Sum = ",add(int(n1),int(n2)));

e_o("Number is ", int(n1))

