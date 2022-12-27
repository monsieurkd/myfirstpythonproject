#codewar practice 
#narcissistic number

# def narcissistic( value ):
    
#     # Code away
#     day = []
    
#     temp = value
#     t = 0
    
#     while temp >=10:
#         so = temp %10
#         temp = int(temp /10)
#         day.append(so)
#     day.append(temp)
#     for i in day:
#         t += i**len(day)
#     if value <10 or value == t:
#         return True 
#     return False


# print(narcissistic(7))
# print(narcissistic(187))
# print(narcissistic(153))
# print(narcissistic(1223))

# def tribonacci(signature, n):
    
#     if n < 3:
#         return signature[:n]
    
#     i=0
#     for i in range(n-3):
#         d = signature[i]+signature[i+1]+ signature[i+2]
#         signature.append(d)
                

#     return signature
#     # so simple yet took me so long 
# print(tribonacci([1,2,3],10))


#                                               string are immutable!!! (in python ofc)
# def disemvowel(string_):
#     for x in string_:
#         d = ['a', 'e','i', 'o', 'u','A', 'E','I', 'O', 'U',]
#         for y in d:
#             if x == y:
#                 string_ =string_.replace(x, '')
#     return string_

# another solution 
# def disemvowel(string):
#    return "".join(c for c in string if c.lower() not in "aeiou")

# print(disemvowel('sdfjskahf aslfdjaklsjd a e i o u'))


# test.describe("Basic tests")
# test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
# test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
# test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
# test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
# test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
# test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
# test.assert_equals(tribonacci([1, 1, 1], 1), [1])
# test.assert_equals(tribonacci([300, 200, 100], 0), [])
# test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])


'''tổng kết 3 vấn đề tribonaci, số ái kỉ và thay string'''