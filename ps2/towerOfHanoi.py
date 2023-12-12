def printMove(fr, to):
    print("move from" + str(fr) + "to" + str(to) )

def Tower(n , fr, to ,spare):
    if n == 1:
        printMove(fr, to)
    else:
        Tower(n-1, fr, spare, to)
        Tower(1, fr, to , spare)
        Tower(n-1, spare, to , fr)

print(Tower(5, ' A ', ' B ', ' C '))