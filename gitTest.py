

def fun1(name):
    print(f"Welcome to git {name}")

def fun2(n):
    for i in range(n):
        print(f"{i+1}.  Welcome")

def fun3(n):
    for i in range (n):
        if (i%2==0):
            status = 'even'
        else:
            status = 'odd'
        print(f"{i} -> i'm {status}")


fun1("ahmed")
fun2(3)
fun3(9)

print("GoodBye")

