def dirReduc(arr):
    new_dir = []
    index = 1
    for i in range(len(arr)-1):

        if arr[i] == "NORTH" and arr[index] == "SOUTH":
            arr.remove(arr[i])
            arr.remove(arr[index])
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))