n=int(input())
m=int(input())
R=range
P=print
d=1
w=(n+1)*4
h=n*2+1
p='+'
M=[[' '] * w for _ in R(h)]
y,x=h-1,-1
def l():
 global d,M;d-=1
 if d==-1:d=3;M[y][x]=p
def r():
 global d,M;d+=1
 if d==4:d=0
 M[y][x]=p
def D(n):
 global M,y,x
 for i in R(n):
  if d==0:
   for i in R(2):y-=1;M[y][x]='|'
  elif d==1:
   for i in R(4):x+=1;M[y][x]='-'
  elif d==2:
   for i in R(2):y+=1;M[y][x]='|'
  else:
   for i in R(4):x-=1;M[y][x]='-'
for i in reversed(R(1,n+1)):
 D(i);l()
 if i==1:D(i)
for i in R(1,n+2):
 r()
 if i==n+1:D(i-1)
 else:D(i)
M[y][x]=p
for r in M:
 for i in R(m):
  for c in r:P(c,end='')
 P()