n=int(input("Enter the length: "))

array=[]

for i in range(n):
    num=int(input(f"Enter the {i+1} number: "))
    array.append(num)
print(f"The array of the size {n} is {array}")
print(f"The max of the elements in {array} is {max(array)}")
print(f"The min of the elements in {array} is {min(array)}")
