"""part00"""
"""---exo1---"""
"""import sys
x = sys.argv[1]
y = sys.argv[2]
n = len(sys.argv)
for i in range (3,n):
    y = y +" "+ sys.argv[i]
if len(sys.argv) == 0:
    print("please write your name")
else:
    print("Your name is:",x,"your last name is:",y)

"""---exo2---"""
import sys
txt = sys.argv[1]
for i in txt:
    if i in "aouie":
        print(i.upper(),end = " ")
    else:
        print(i,end = " ")

"""---exo3---"""
def sum(x,y):
    z = x + y
    print("sum is :", z)

def multi(x,y):
    s = x * y 
    print("multiplication is",s)

"""---exo4---"""
def Nospace(x,y,z):
    a = x + y + z
    print(a)"""

"""---exo5---"""
def num_10():
    x = 1
    while(x < 10):
        print(x,"\n")
        x += 1
num_10()

