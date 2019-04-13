#1
a = (input("dãy số: "))
b = a.split()
for i in range(len(b)):
    print(b[i])
#2    
a = input("dãy số: ")
b = a.split()
print("có những cặp số tích bằng 128:")
for i in range(len(b)):
    for j in range(len(b)):
        if int(b[i])*int(b[j])==128:
            if i<j:
                print(b[i], "và", b[j], "tại ví trí", i+1, "và", j+1)
            
        