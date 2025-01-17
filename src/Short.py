from collections import deque;import time;R=4;C=3;c=[[1,2,0,1],[0,0,0,0],[1,4,0,1],[0,3,3,0],[3,0,0,3]]
d=[["   ","   "],["┌–┐","| |","| |","└–┘",],["┌––––┐","|    |","|    |","└––––┘",],["┌–┐","└–┘",],["┌––––┐","└––––┘"]]
r=print;n=range;e=enumerate;G=tuple;z=list;t=int;Y=len;T=map;P=set;L=deque;S=time.perf_counter;s=chr;A=None;M=input
def h(c:z[z],i): return G(G(q) for q in c) if not i else [z(T(t,q)) for q in c]
def p(c:z[z]):
    r(s(10));E=[[" "] * 12 for _ in n(10)]
    for q in n(R+1):
        for x in n(C+1):
            for j, f in e(d[c[q][x]]):
                if c[q][x]>0:
                    for h, g in e(f):E[q*2+j][x*3+h]=g
    for i in E:r("".join(i))
def l(B:z[z]):
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
def m(c:z[z],g:z[z]):
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
def ds(c:z[z]):
    c=[z(T(lambda x:x if x>0 else 0,c[i])) for i in n(Y(c))]
    for q,i in e(c):
        for x,t in e(i):
            if t==1:c[q+1][x]=-c[q][x]
            if t==2:c[q+1][x]=-c[q][x];c[q][x+1]=-c[q][x];c[q+1][x+1]=-c[q][x]
            if t==4:c[q][x+1]=-c[q][x]
    return c
def bfs():
    U=L([[(c,0,[(0,0),(0,0)])]]);v=P();v.add(h(c,0))
    while U:
        k=U.popleft();w=h(k[-1][0],1);t=k[-1][1]
        if w[3][1]==2: return k
        for g in l(w):
            I=m(h(w,0),g);o=h(I,0)
            if not v.__contains__(o): v.add(o);U.append(k+[(o,t+1,g)])
c=ds(c);r("Shortest path:");p(h(c,1));t1=S();O=bfs()
if O!=A:
    r(f"time taken: {(S()-t1)*1000:0.2f}ms")
    for i in O:M(f"move: {i[2]}");p(h(i[0],1))