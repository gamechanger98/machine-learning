from math import *
#acid=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
s1 = {'A':0.62, 'C':0.29, 'D':-0.9, 'E':-0.74, 'F':1.19, 'G':0.48, 'H':-0.4, 'I':1.38, 'K':-1.5, 'L':1.06, 'M':0.64, 'N':-0.78, 'P':0.12, 'Q':-0.85, 'R':-2.53, 'S':-0.18, 'T':-0.05, 'V':1.08, 'W':0.81, 'Y':0.26}
s2={'A':-0.5, 'C':-1, 'D':3, 'E':3, 'F':-2.5, 'G':0, 'H':-0.5, 'I':-1.8, 'K':3, 'L':-1.8, 'M':-1.3, 'N':0.2, 'P':0, 'Q':0.2, 'R':3, 'S':0.3, 'T':-0.4, 'V':-1.5, 'W':-3.4, 'Y':-2.3}
t1={'A':15, 'C':47, 'D':59, 'E':73, 'F':91, 'G':1, 'H':82, 'I':57, 'K':73, 'L':57, 'M':75, 'N':58, 'P':42, 'Q':72, 'R':101, 'S':31, 'T':45, 'V':43, 'W':130, 'Y':107}
#p="ACD"
#print(s1[p[0]])
def polypeptide(p, acid):
    d=len(p)
    delta=[]
#op=[]
    s=0
    for k in range(1,min(d,51)):

        for i in range(0,(d-k)):

            j=i+k
            dv=((pow((s1[p[j]]-s1[p[i]]),2)+pow((s2[p[j]]-s2[p[i]]),2)+pow((t1[p[j]]-t1[p[i]]),2))/3)
            s+=dv

        s=s/(d-k)

        delta.append(s)
        s=0
#print(delta)
    u=sum(delta)
    freq=[]
    for i in range(20):
        f=p.count(acid[i])
        freq.append(f)
    e=sum(freq)
    t=0.05*u+e
#print(t)
    list1=[]
    for i in range(20):
        v=freq[i]/t
        list1.append(v)
    for i in range(0,len(delta)):
        h=(0.05*delta[i])/t
        list1.append(h)
    return list1



