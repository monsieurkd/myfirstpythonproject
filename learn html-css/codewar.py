 
def move_zeros(lst):
    temp = ""
    for i, x in enumerate(lst):
        for i, x in  enumerate(lst):
            if x == 0:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                
            
    return lst

lst1 = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

print(move_zeros(lst1))