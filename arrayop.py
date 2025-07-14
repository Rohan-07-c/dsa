# Initialize an array (list)
n=int(input("Enter the value of n: "))
arr=[]

for i in range(n):
    num=int(input(f"Enter the {i+1} number: "))
    arr.append(num)
print(f"The array of the size {n} is {arr}")


# 1. Traversal
print("Original Array:")
for i in arr:
    print(i, end=' ')
print("\n")

# 2. Insertion
arr.insert(2, 7)  # Insert 25 at index 2
print("After Insertion at index 2:")
print(arr)

# 3. Deletion



del arr[2]  # Remove the value 40
print("After Deletion at index 2:")
print(arr)

arr.remove(9)
print(arr)

# 4. Searching
search_val = 8
if search_val in arr:
    print(f"Value {search_val} found at index {arr.index(search_val)}")
else:
    print(f"Value {search_val} not found in array.")

# 5. Updating
arr[3] = 4  # Update index 3 to new value
print("After Updating index 3 to 4:")
print(arr)