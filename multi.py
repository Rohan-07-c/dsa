# 3D array: 2 blocks, each with 2 rows and 3 columns
array_3d = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [9, 1, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12],
        [3, 9, 4]
    ]
]

print("3D Array Elements:")
for i in range(len(array_3d)):
    for j in range(len(array_3d[i])):
        for k in range(len(array_3d[i][j])):
            print(f"Element at [{i}][{j}][{k}] = {array_3d[i][j][k]}")
