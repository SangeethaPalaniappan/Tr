#Pattern
n=int(input("N:"))

for i in range(n+2):
    
    print("*","\t",end="")
while n!=0: 
    print("\n","*",n*"\t","*")
    n-=1
print("\n","*")
