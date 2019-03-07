
"""Pseudo Amino Acid Composition"""
import math 

Hydrophobicity = {'A':0.62, 'C':0.29, 'D':-0.9, 'E':-0.74, 'F':1.19, 'G':0.48, 'H':-0.4, 'I':1.38, 'K':-1.5, 'L':1.06, 'M':0.64, 'N':-0.78, 'P':0.12, 'Q':-0.85, 'R':-2.53, 'S':-0.18, 'T':-0.05, 'V':1.08, 'W':0.81, 'Y':0.26,'B':0,'J':0,'O':0,'U':0,'X':0,'Z':0}
Hydrophilicity={'A':-0.5, 'C':-1, 'D':3, 'E':3, 'F':-2.5, 'G':0, 'H':-0.5, 'I':-1.8, 'K':3, 'L':-1.8, 'M':-1.3, 'N':0.2, 'P':0, 'Q':0.2, 'R':3, 'S':0.3, 'T':-0.4, 'V':-1.5, 'W':-3.4, 'Y':-2.3,'B':0,'J':0,'O':0,'U':0,'X':0,'Z':0}
Side_chain_mass ={'A':15, 'C':47, 'D':59, 'E':73, 'F':91, 'G':1, 'H':82, 'I':57, 'K':73, 'L':57, 'M':75, 'N':58, 'P':42, 'Q':72, 'R':101, 'S':31, 'T':45, 'V':43, 'W':130, 'Y':107,'B':0,'J':0,'O':0,'U':0,'X':0,'Z':0}
        
def pseudo(S, V):
    def couplingfactor(i,j):
#        print(i,j)
#        print(S[i])
#        print(S[j])
#        print("##################################")
        A1=S[i]
        A2=S[j]
        S1=Hydrophobicity[A1]
        S2=Hydrophobicity[A2]
        S3=Hydrophilicity[A1]
        S4=Hydrophilicity[A2]
        T1=Side_chain_mass[A1]
        T2=Side_chain_mass[A2]
        j=(math.pow((S2-S1),2)+math.pow((S4-S3),2)+math.pow((T2-T1),2))/3
        return j

    list=[]
    sequenceOrderInf=0
    for k in range(1,min(len(S),51)):
        for i in range(0,(len(S)-k)):
            sequenceOrderInf+=couplingfactor(i,i+k)
        sequenceOrderInf=sequenceOrderInf/(len(S)-k)
        list.append(sequenceOrderInf)
        sequenceOrderInf=0
        
    deltaSum=sum(list)
    
    """Amino Acid Frequency """
    list1=[]
    w = 0.05
    for i in range(0,20):
        p=S.count(V[i])
        list1.append(p)
        
    frqSum=sum(list1)
    total = (w * deltaSum) + frqSum
    
    """Normalize and Final vector"""
    final_seq_vec = []
    for i in range(0,20):
        q = list1[i] / total
        final_seq_vec.append(q)  
    
    for i in range(0,len(list)):
        q = (w * list[i]) / total
        final_seq_vec.append(q)
        
    return final_seq_vec
    
    

    
     
        