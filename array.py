
n=int(input("Enter the value of n: "))
array=[]

for i in range(n):
    num=int(input(f"Enter the {i+1} number: "))
    array.append(num)
print(f"The array of the size {n} is {array}")

h=int(input("Enter the index value: "))

if h<n:
    arr=array[h]
    print(f"The value at index value {h} is {arr}")
else:
    print("Index not found")
    
