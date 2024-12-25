from collections import deque;import time;R=4;C=3;c=[[1,2,0,1],[0,0,0,0],[1,4,0,1],[0,3,3,0],[3,0,0,3]]
d=[["   ","   "],["┌–┐","| |","| |","└–┘",],["┌––––┐","|    |","|    |","└––––┘",],["┌–┐","└–┘",],["┌––––┐","└––––┘"]]
r=print;n=range;e=enumerate;tp=tuple;z=list;t=int;ln=len;mp=map;st=set;dq=deque;tm=time.perf_counter
def h(c:z,i)->tp:
    return tp(tp(q) for q in c) if not i else [z(mp(t,q)) for q in c]
def p(c:z)->None:
    r("\n");nb=[[" "] * 12 for _ in n(10)]
    for q in n(R+1):
        for x in n(C+1):
            if c[q][x]>0:
                for j, f in e(d[c[q][x]]):
                    for h, g in e(f):nb[q*2+j][x*3+h]=g
    for i in nb:r("".join(i))
def l(ps:z)->z:
    m=[]; u=m.append
    for q,i in e(ps):
        for x,t in e(i):
            if t==1 and x!=C and (ps[q+1][x+1]==0 and ps[q][x+1]==0):u([(q,x),(q,x+1)])
            if t==1 and x!=0 and (ps[q+1][x-1]==0 and ps[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==1 and q!=R-1 and (ps[q+2][x]==0):u([(q,x),(q+1,x)])
            if t==1 and q!=0 and (ps[q-1][x]==0):u([(q,x),(q-1,x)])
            if t==2 and x!=C-1 and (ps[q+1][x+2]==0 and ps[q][x+2]==0):u([(q,x),(q,x+1)])
            if t==2 and x!=0 and (ps[q+1][x-1]==0 and ps[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==2 and q!=R-1 and (ps[q+2][x]==0 and ps[q+2][x+1]==0):u([(q,x),(q+1,x)])
            if t==2 and q!=0 and (ps[q-1][x]==0 and ps[q-1][x+1]==0):u([(q,x),(q-1,x)])
            if t==3 and x!=C and (ps[q][x+1]==0):u([(q,x),(q,x+1)])
            if t==3 and x!=0 and (ps[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==3 and q!=R and (ps[q+1][x]==0):u([(q,x),(q+1,x)])
            if t==3 and q!=0 and (ps[q-1][x]==0):u([(q,x),(q-1,x)])
            if t==4 and x!=C-1 and (ps[q][x+2]==0):u([(q,x),(q,x+1)])
            if t==4 and x!=0 and (ps[q][x-1]==0):u([(q,x),(q,x-1)])
            if t==4 and q!=R and (ps[q+1][x]==0 and ps[q+1][x+1]==0):u([(q,x),(q+1,x)])
            if t==4 and q!=0 and (ps[q-1][x]==0 and ps[q-1][x+1]==0):u([(q,x),(q-1,x)])
    return m
def m(c:z,g:z)->z:
    c=h(c,1);t=c[g[0][0]][g[0][1]];m=(g[1][0] - g[0][0]);b=(g[1][1] - g[0][1]);c[g[1][0]][g[1][1]]=c[g[0][0]][g[0][1]];c[g[0][0]][g[0][1]]=0
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
def ds(c:z):
    c=[z(mp(lambda x:x if x>0 else 0,c[i])) for i in n(ln(c))]
    for q,i in e(c):
        for x,t in e(i):
            if t==1:c[q+1][x]=-c[q][x]
            if t==2:c[q+1][x]=-c[q][x];c[q][x+1]=-c[q][x];c[q+1][x+1]=-c[q][x]
            if t==4:c[q][x+1]=-c[q][x]
    return c
def bfs()->z|t:
    ck=dq([[(c,0,[(0,0),(0,0)])]]);v=st();v.add(h(c,0))
    while ck:
        k=ck.popleft();w=h(k[-1][0],1);t=k[-1][1]
        if w[3][1]==2: return k
        for g in l(w):
            nr=m(h(w,0),g);o=h(nr,0)
            if not v.__contains__(o): v.add(o);ck.append(k + [(o,t + 1,g)])
c=ds(c);r("\n\nINITIAL POSITION");p(h(c,1));t1=tm();ns=bfs()
if ns!=None:
    r(f"Shortest path length: {ns[-1][1]}\nTime Taken: {(tm() - t1)*1000:0.2f} ms")
    for i in ns:input("Press Enter for next move: \n");r(f"Move: {i[2]}");p(h(i[0],1))