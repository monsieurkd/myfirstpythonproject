def solution(var):
    firstList = []
    secondList = [] 

    for i in range(len(var)-1):
        x = 1 

        while True:
         
            if var[0] + x == var[0+x]:
                firstList.append(var[i])
                x += 1
                
                
            else:
                
                break
            
            
    return firstList

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

