from __future__ import print_function
import random
import math

def schaff(s):                                                                  #Scahffer function
    f1 = math.pow(s, 2)
    f2 = math.pow((s - 2), 2)
    eschaff = f1 + f2
    return eschaff

def min_max():                                                                  #calc min & max Schaffer for Normalization
    values = []
    for i in range(100):
        values.append(schaff(random.randint(-100000, 100000)))
    mini = min(values)
    maxi = max(values)
    return (mini,maxi)
    # print("min:{} max:{}".format(mini, maxi))

def energyfunc(s,min,max):                                                      #calculate normalized Schaffer of a state
    schaff_val=schaff(s)
    norm_schaff=(schaff_val-min)/(max-min)
    return  norm_schaff

def neighbour(s):                                                               #pick next state
    sn= random.uniform(s*0.9, s*1.1)
    return sn

def crazyjump(e,en,t):                                                          #calculate probability of crazy jump
    jmp_prob=math.exp((e-en)/t)
    return jmp_prob

def simannealer():
    state= random.randint(-100000,100000)
    k=1                                                                         #initializations
    kmax=1000
    emax=-1
    scahff_minmax = min_max()                                                   #Schaffer baseline max & min
    min = scahff_minmax[0]                                                      
    max = scahff_minmax[1]
    energy = energyfunc(state,min,max)                                          #initial state energy
    beststate = state
    bestenergy = energy
    print("\n, %04d, :%3.5f " % (k, bestenergy), end="")
    while k<kmax and energy>emax:                                               #loop invariant
        nextstate=neighbour(state)
        nextenergy=energyfunc(nextstate,min, max)
        if nextenergy<bestenergy:                                               #make next state and next energy as the best state and best enrgy
            beststate=nextstate
            bestenergy=nextenergy
            print('!',end="")

        if nextenergy<energy:                                                   #make next state and next energy as the current state and current energy
            state=nextstate
            energy=nextenergy
            print('+',end="")

        elif nextenergy>energy:                                                 #decision on crazy jump 
            prob_crazyjump=crazyjump(energy,nextenergy, k/kmax)
            if prob_crazyjump<random.randint(0,1):
                state=nextstate
                energy=nextenergy
                print("?", end="")
        print(".", end="")
        k=k+1
        if k%25==0:
            print("\n, %04d, :%3.5f " % (k, bestenergy), end="")
    print("\n")                                                                 #report end state and end energy
    print("beststate:{}".format(beststate))
    print("k:{}".format(k))
    print("bestenergy:{}".format(bestenergy))



simannealer()


