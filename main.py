n = int(input("Введите кол-во чисел"))

arr = []
for i in range(n):
    arr.append(input())

for i in range(n-1):
    for j in range(n-i-1):
        if(arr[j]>arr[j+1]):
            b = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = b

print(arr)