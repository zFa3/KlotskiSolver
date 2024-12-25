# this is a joke, no convections are followed BUT still completely functional program
from collections import deque;import time;R=4;C=3;c=[[1,2,0,1],[0,0,0,0],[1,4,0,1],[0,3,3,0],[3,0,0,3]]
d=[["   ","   "],["┌–┐","| |","| |","└–┘",],["┌––––┐","|    |","|    |","└––––┘",],["┌–┐","└–┘",],["┌––––┐","└––––┘"]]
r=print;n=range;e=enumerate;G=tuple;z=list;t=int;Y=len;T=map;P=set;L=deque;S=time.perf_counter;s=chr;A=None;M=input
def h(c:z[z],i)->G: return G(G(q) for q in c) if not i else [z(T(t,q)) for q in c]
def p(c:z[z])->A:
    r(s(10));E=[[" "] * 12 for _ in n(10)]
    for q in n(R+1):
        for x in n(C+1):
            for j, f in e(d[c[q][x]]):
                if c[q][x]>0:
                    for h, g in e(f):E[q*2+j][x*3+h]=g
    for i in E:r("".join(i))
def l(B:z[z])->z[z]:
    m=[]; u=m.append
    for q,i in e(B):
        for x,t in e(i):
            if t==1 and x!=C and (B[q+1][x+1]==0 and B[q][x+1]==0):u([(q,x),(q,x+1)])
            if t==1 and x!=0 and (B[q+1][x-1]==0 and B[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==1 and q!=R-1 and (B[q+2][x]==0):u([(q,x),(q+1,x)])
            if t==1 and q!=0 and (B[q-1][x]==0):u([(q,x),(q-1,x)])
            if t==2 and x!=C-1 and (B[q+1][x+2]==0 and B[q][x+2]==0):u([(q,x),(q,x+1)])
            if t==2 and x!=0 and (B[q+1][x-1]==0 and B[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==2 and q!=R-1 and (B[q+2][x]==0 and B[q+2][x+1]==0):u([(q,x),(q+1,x)])
            if t==2 and q!=0 and (B[q-1][x]==0 and B[q-1][x+1]==0):u([(q,x),(q-1,x)])
            if t==3 and x!=C and (B[q][x+1]==0):u([(q,x),(q,x+1)])
            if t==3 and x!=0 and (B[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==3 and q!=R and (B[q+1][x]==0):u([(q,x),(q+1,x)])
            if t==3 and q!=0 and (B[q-1][x]==0):u([(q,x),(q-1,x)])
            if t==4 and x!=C-1 and (B[q][x+2]==0):u([(q,x),(q,x+1)])
            if t==4 and x!=0 and (B[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==4 and q!=R and (B[q+1][x]==0 and B[q+1][x+1]==0):u([(q,x),(q+1,x)])
            if t==4 and q!=0 and (B[q-1][x]==0 and B[q-1][x+1]==0):u([(q,x),(q-1,x)])
    return m
def m(c:z[z],g:z[z])->z[z]:
    c=h(c,1);t=c[g[0][0]][g[0][1]];m=(g[1][0]-g[0][0]);b=(g[1][1]-g[0][1]);c[g[1][0]][g[1][1]]=c[g[0][0]][g[0][1]];c[g[0][0]][g[0][1]]=0
    if t==1 and m==1:c[g[0][0]][g[0][1]]=0;c[g[1][0]+1][g[1][1]]=-1
    if t==1 and m==-1:c[g[0][0]+1][g[0][1]]=0;c[g[0][0]][g[0][1]]=-1
    if t==1 and b==1:c[g[1][0]+1][g[1][1]]=-1;c[g[0][0]+1][g[0][1]]=0
    if t==1 and b==-1:c[g[1][0]+1][g[1][1]]=-1;c[g[0][0]+1][g[0][1]]=0
    if t==2 and m==1:c[g[0][0]][g[0][1]]=0;c[g[0][0]][g[0][1]+1]=0;c[g[1][0]+1][g[1][1]]=-2;c[g[1][0]+1][g[1][1]+1]=-2
    if t==2 and m==-1:c[g[0][0]+1][g[0][1]]=0;c[g[0][0]+1][g[0][1]+1]=0;c[g[0][0]][g[0][1]]=-2;c[g[0][0]][g[0][1]+1]=-2;c[g[1][0]][g[1][1]+1]=-2
    if t==2 and b==1:c[g[0][0]][g[0][1]]=0;c[g[1][0]][g[1][1]+1]=-2;c[g[0][0]+1][g[0][1]]=0;c[g[1][0]+1][g[1][1]+1]=-2
    if t==2 and b==-1:c[g[0][0]][g[0][1]+1]=0;c[g[0][0]][g[0][1]]=-2;c[g[0][0]+1][g[0][1]+1]=0;c[g[0][0]+1][g[0][1]]=-2;c[g[1][0]+1][g[1][1]]=-2
    if t==4 and b==1:c[g[0][0]][g[0][1]]=0;c[g[1][0]][g[1][1]+1]=-4
    if t==4 and b==-1:c[g[0][0]][g[0][1]+1]=0;c[g[0][0]][g[0][1]]=-4
    if t==4 and m==1:c[g[0][0]][g[0][1]+1]=0;c[g[1][0]][g[1][1]+1]=-4
    if t==4 and m==-1:c[g[0][0]][g[0][1]+1]=0;c[g[1][0]][g[1][1]+1]=-4
    return c
def ds(c:z[z])->z[z]:
    c=[z(T(lambda x:x if x>0 else 0,c[i])) for i in n(Y(c))]
    for q,i in e(c):
        for x,t in e(i):
            if t==1:c[q+1][x]=-c[q][x]
            if t==2:c[q+1][x]=-c[q][x];c[q][x+1]=-c[q][x];c[q+1][x+1]=-c[q][x]
            if t==4:c[q][x+1]=-c[q][x]
    return c
def bfs()->z[z]|A:
    U=L([[(c,0,[(0,0),(0,0)])]]);v=P();v.add(h(c,0))
    while U:
        k=U.popleft();w=h(k[-1][0],1);t=k[-1][1]
        if w[3][1]==2: return k
        for g in l(w):
            I=m(h(w,0),g);o=h(I,0)
            if not v.__contains__(o): v.add(o);U.append(k+[(o,t+1,g)])
c=ds(c);r(s(10)+s(10)+s(73)+s(78)+s(73)+s(84)+s(73)+s(65)+s(76)+s(32)+s(80)+s(79)+s(83)+s(73)+s(84)+s(73)+s(79)+s(78));p(h(c,1));t1=S();O=bfs()
if O!=A:
    r(s(83)+s(104)+s(111)+s(114)+s(116)+s(101)+s(115)+s(116)+s(32)+s(112)+s(97)+s(116)+s(104)+s(32)+s(108)+s(101)+s(110)+s(103)+s(116)+s(104)+s(58)+s(32)+f"{O[-1][1]}"+s(10)+s(84)+s(105)+s(109)+s(101)+s(32)+s(84)+s(97)+s(107)+s(101)+s(110)+s(58)+s(32)+f"{(S()-t1)*1000:0.2f}"+s(32)+s(109)+s(115))
    for i in O:M(s(80)+s(114)+s(101)+s(115)+s(115)+s(32)+s(69)+s(110)+s(116)+s(101)+s(114)+s(32)+s(102)+s(111)+s(114)+s(32)+s(110)+s(101)+s(120)+s(116)+s(32)+s(109)+s(111)+s(118)+s(101)+s(58)+s(32)+s(10));r(s(109)+s(111)+s(118)+s(101)+s(58)+s(32)+f"{i[2]}");p(h(i[0],1))