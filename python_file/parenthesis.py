a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
def dirReduc(arr):
    
    while True:
        for i in range(len(arr)+1):
            if( arr[i] == "NORTH" and arr[i+1] == "SOUTH") or ( arr[i] == "SOUTH" and arr[i+1] == "NORTH"):
                arr.pop(i)
                arr.pop(i)
            elif ( arr[i] == "EAST" and arr[i+1] == "WEST") or ( arr[i] == "WEST" and arr[i+1] == "EAST"):
                arr.pop(i)
                arr.pop(i)
        
dirReduc(a)
