
L = ["http://www.codewars.com/kata/", "icann.org", "https://youtube.com" , "http://codewars.com" , "https://hyphen-site.org", "https://123.net", "http://google.co.jp", "http://google.com"]

splitVar = ["/", ".", ":", "-", "www"]
for i in L:
    print(i.split("//")[-1].split("www.")[-1].split(".")[0]
)
    

