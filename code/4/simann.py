import random
import math

def schaff(s):
    f1 = math.pow(s, 2)
    f2 = math.pow((s - 2), 2)
    eschaff = f1 + f2
    return eschaff

def schaffminmax():
    run = 0
    max=0.0
    min=0.0
    for run in range(1, 101):
        schaff_input = random.randint(1,100)
        eschaff=schaff(schaff_input)
        if max < eschaff:
            max = eschaff
        if min > eschaff:
            min = eschaff
    return (min, max)

def energyfunc(s,min,max):
    schaff_val=schaff(s)
    norm_schaff=(schaff_val-min)/(max-min)
    return  norm_schaff



def neighbour(s):
    sn= random.uniform(s+1.1,s+0.9)
    return sn

def crazyjump(e,en,t):
    jmp_prob=math.exp((en-e)/t)

def simannler():
    state= random.randint((-10)**5,(10)**5)
    k=0.0
    kmax=1000
    emax=-1
    scahff_minmax = schaffminmax()
    min = scahff_minmax[0]
    max = scahff_minmax[1]
    energy = energyfunc(state,min,max)
    beststate = state
    bestenergy = energy
    while k<kmax and energy>emax:
        nextstate=neighbour(state)
        nextenergy=energyfunc(nextstate,min, max)
        if nextenergy<bestenergy:
            beststate=nextstate
            bestenergy=nextenergy
            print('!',end="")

        if nextenergy<energy:
            state=nextstate
            energy=nextenergy
            print('+',end="")

        elif nextenergy>energy:
            prob_crazyjump=crazyjump(energy,nextenergy, k/kmax)
            if prob_crazyjump<random.randint():
                state=nextstate
                energy=nextenergy
                print("?", end="")
        print(".")
        k=k+1
        if k%50==0:
             print("\n")
             print(beststate)

simannler();
