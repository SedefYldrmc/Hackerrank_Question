#soru1 => Array and strings
T=int(input(""))
while T>0:
    txt=input("" )#dizi eleman sayısı=,dönme sayısı
    s=[]
    for i in txt:
        s.append(i)
    N=int(s[0])
    K=int(s[2])
    a=input("dize=") # dize elemanları
    A=[]
    for x in a:
        A.append(int(x))
    for i in range(K):
        B=[]
        B.append(A[-1])
        for x in range(N-1):
            B.append(A[x])
        A=B
        B=[]
    T-=1        
print(A)      
