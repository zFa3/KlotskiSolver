from collections import deque;import time as tm;ROW=4;COL=3;c=[[1,2,0,1],[0,0,0,0],[1,4,0,1],[0,3,3,0],[3,0,0,3]]
pieces=[["   ","   "],["┌–┐","| |","| |","└–┘",],["┌––––┐","|    |","|    |","└––––┘",],["┌–┐","└–┘",],["┌––––┐","└––––┘"]]
r=print;rn=range;en=enumerate;tp=tuple;st=list;t=int
def h(c:st,reverse)->tp:
    return tp(tp(q) for q in c) if not reverse else [st(map(t,q)) for q in c]
def p(c:st) -> None:
    r("\n");nb = [[" "] * 12 for _ in rn(10)]
    for q in rn(ROW+1):
        for x in rn(COL+1):
            if c[q][x]>0:
                for row, item in en(pieces[c[q][x]]):
                    for col, character in en(item):nb[q*2+row][x*3+col] = character
    for i in nb:r("".join(i))
def l(ps:st)->st:
    lm=[]; ap=lm.append
    for q,i in en(ps):
        for x,pt in en(i):
            if pt==1 and x!=COL and (ps[q+1][x+1]==0 and ps[q][x+1]==0):ap([(q,x),(q,x+1)]) 
            if pt==1 and x!=0 and (ps[q+1][x-1]==0 and ps[q][x-1]==0):ap([(q,x),(q,x-1)]) 
            if pt==1 and q!=ROW-1 and (ps[q+2][x]==0):ap([(q,x),(q+1,x)]) 
            if pt==1 and q!=0 and (ps[q-1][x]==0):ap([(q,x),(q-1,x)]) 
            if pt==2 and x!=COL-1 and (ps[q+1][x+2]==0 and ps[q][x+2]==0):ap([(q,x),(q,x+1)]) 
            if pt==2 and x!=0 and (ps[q+1][x-1]==0 and ps[q][x-1]==0):ap([(q,x),(q,x-1)]) 
            if pt==2 and q!=ROW-1 and (ps[q+2][x]==0 and ps[q+2][x+1]==0):ap([(q,x),(q+1,x)]) 
            if pt==2 and q!=0 and (ps[q-1][x]==0 and ps[q-1][x+1]==0):ap([(q,x),(q-1,x)]) 
            if pt==3 and x!=COL and (ps[q][x+1]==0):ap([(q,x),(q,x+1)]) 
            if pt==3 and x!=0 and (ps[q][x-1]==0):ap([(q,x),(q,x-1)]) 
            if pt==3 and q!=ROW and (ps[q+1][x]==0):ap([(q,x),(q+1,x)]) 
            if pt==3 and q!=0 and (ps[q-1][x]==0):ap([(q,x),(q-1,x)]) 
            if pt==4 and x!=COL-1 and (ps[q][x+2]==0):ap([(q,x),(q,x+1)]) 
            if pt==4 and x!=0 and (ps[q][x-1]==0):ap([(q,x),(q,x-1)]) 
            if pt==4 and q!=ROW and (ps[q+1][x]==0 and ps[q+1][x+1]==0):ap([(q,x),(q+1,x)]) 
            if pt==4 and q!=0 and (ps[q-1][x]==0 and ps[q-1][x+1]==0):ap([(q,x),(q-1,x)])
    return lm
def m(c:st,mv:st)->st:
    c=h(c,1);pt=c[mv[0][0]][mv[0][1]];yd=(mv[1][0] - mv[0][0]);xd=(mv[1][1] - mv[0][1]);c[mv[1][0]][mv[1][1]]=c[mv[0][0]][mv[0][1]];c[mv[0][0]][mv[0][1]]=0
    if pt==1 and yd==1:c[mv[0][0]][mv[0][1]]=0;c[mv[1][0]+1][mv[1][1]]=-1
    if pt==1 and yd==-1:c[mv[0][0]+1][mv[0][1]]=0;c[mv[0][0]][mv[0][1]]=-1
    if pt==1 and xd==1:c[mv[1][0]+1][mv[1][1]]=-1;c[mv[0][0]+1][mv[0][1]]=0
    if pt==1 and xd==-1:c[mv[1][0]+1][mv[1][1]]=-1;c[mv[0][0]+1][mv[0][1]]=0
    if pt==2 and yd==1:c[mv[0][0]][mv[0][1]]=0;c[mv[0][0]][mv[0][1]+1]=0;c[mv[1][0]+1][mv[1][1]]=-2;c[mv[1][0]+1][mv[1][1]+1]=-2
    if pt==2 and yd==-1:c[mv[0][0]+1][mv[0][1]]=0;c[mv[0][0]+1][mv[0][1]+1]=0;c[mv[0][0]][mv[0][1]]=-2;c[mv[0][0]][mv[0][1]+1]=-2;c[mv[1][0]][mv[1][1]+1]=-2
    if pt==2 and xd==1:c[mv[0][0]][mv[0][1]]=0;c[mv[1][0]][mv[1][1]+1]=-2;c[mv[0][0]+1][mv[0][1]]=0;c[mv[1][0]+1][mv[1][1]+1]=-2
    if pt==2 and xd==-1:c[mv[0][0]][mv[0][1]+1]=0;c[mv[0][0]][mv[0][1]]=-2;c[mv[0][0]+1][mv[0][1]+1]=0;c[mv[0][0]+1][mv[0][1]]=-2;c[mv[1][0]+1][mv[1][1]]=-2
    if pt==4 and xd==1:c[mv[0][0]][mv[0][1]]=0;c[mv[1][0]][mv[1][1]+1]=-4
    if pt==4 and xd==-1:c[mv[0][0]][mv[0][1]+1]=0;c[mv[0][0]][mv[0][1]]=-4
    if pt==4 and yd==1:c[mv[0][0]][mv[0][1]+1]=0;c[mv[1][0]][mv[1][1]+1]=-4
    if pt==4 and yd==-1:c[mv[0][0]][mv[0][1]+1]=0;c[mv[1][0]][mv[1][1]+1]=-4
    return c
def ds(c:st):
    c=[st(map(lambda x:x if x>0 else 0,c[i])) for i in rn(len(c))]
    for q,i in en(c):
        for x,pt in en(i):
            if pt==1:c[q+1][x]=-c[q][x]
            if pt==2:c[q+1][x]=-c[q][x];c[q][x+1]=-c[q][x];c[q+1][x+1]=-c[q][x]
            if pt==4:c[q][x+1]=-c[q][x]
    return c
def bfs()->st|t:
    ck=deque([[(c,0,[(0,0),(0,0)])]]);v=set();v.add(h(c,0))
    while ck:
        k=ck.popleft();w=h(k[-1][0],1);pt=k[-1][1]
        if w[3][1]==2: return k
        for mv in l(w):
            nr=m(h(w,0),mv);o=h(nr,0)
            if not v.__contains__(o): v.add(o);ck.append(k + [(o,pt + 1,mv)])
c=ds(c);r("\n\nINITIAL POSITION");p(h(c,1));t1=tm.perf_counter();this=bfs()
if this!=None:
    r(f"Shortest path length: {this[-1][1]}\nTime Taken: {(tm.perf_counter() - t1)*1000:0.2f} ms")
    for i in this:input("Press Enter for next mv: \n");r(f"Move: {i[2]}");p(h(i[0],1))