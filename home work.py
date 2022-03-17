def getFactors(n):  
    fctrs=[];
    for i in range(1, n + 1):
        if n % i == 0:
            fctrs.append(i)
    return fctrs
   
def getPGCD(a,b):   
  a=eval(input("Valeur de a ?")) 
  b=eval(input("Valeur de b ?")) 
  while a!=b: 
    d=abs(b-a) 
    b=a 
    a=d 
  print("pgcd=",d) 
  if d==1: 
    print("Les deux entiers sont premiers entre eux.")

def cinMatch(n):
  l=[]
  h=[]
  for i in range(n):
    l.append(input())
  m=int(input())
  for j in range(m):
    h.append(input().split(','))
    
  for x in l:
    for i in range(m):
        if h[i][0]==x:
            print(','.join(h[i]))
