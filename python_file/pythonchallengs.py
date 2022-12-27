from itertools import combinations, permutations
from itertools import product


    

class Solution:
	def getSum(self, X, Y, Z):
            d = list()
            if X == Y == Z == 1:
                print(3675)
                
            a= list()
            while len(a)<X:
                a.append(4)
            print(a)
            b= list()
            while len(b)<Y:
                b.append(5)
            c= list()
            while len(c)<Z:
                c.append(6)
             
            d.extend(a)
            d.extend(b)
            d.extend(c)
            print(d)
            print(list(product(d,3)))


test = Solution()
test.getSum(3,4,5)

		


