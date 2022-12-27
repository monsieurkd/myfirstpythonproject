def solve(s):
    bracket=["(",")"]
    open=[]
    close=[]
    s = list(s)
    dc = dict()

    
    for par, x in enumerate(s):
        if x== bracket[0]:
            open.append(par)
        if x == ")":
            k = open.pop()
            dc.update({k:par})
            
    
#[index for (index, letter) in enumerate(word) if letter == 'e']
#res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
    #
    for x,y in dc.items():
        for b in range(x+1,y):
            if s[x-1]=='-':
                if s[b] == '-' :
                    s[b] = '+'
                elif s[b]== '+':
                    s[b] ='-'
        s[x] =''
        s[y] =''
    

    for i in range(len(s)):
        if (s[i]== '-' and s[i+1]=='-') or (s[1] == '+'and s[i+1] == '+'):
            s[i] = ''
        if (s[i]== '-' and s[i+1]=='+') or (s[1] == '+'and s[i+1] == '-'):
            s[i] ='-'
            s[i+1] =''
    for i in s:
        if i == "" :    
            s.remove(i)

    s = ''.join(s)   
    print(s) 
        
def congtru(s):
    
    
                


solve("x-(-((-((((-((-(-(-y)))))))))))")          
#             if s[s.index(openbracket)-1] == "+":
#                 #pha ngoặc với dấu dương
#                 s = s.replace(openbracket,'')
#                 s = s.replace(closebracket,'')
                
#             for i in range(s.index(openbracket)+1,s.index(closebracket) ):
#                 if s[s.index(openbracket)-1] == "-":
#                 #pha ngoặc với dấu âm
                    
#                     s = s.replace(openbracket,'')
#                     s = s.replace(closebracket,'')
#                     s = s.replace("+", "-")
#                     s = s.replace("-", "+")
#                     print(s)
        

