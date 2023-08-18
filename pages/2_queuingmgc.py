import math
import numpy as np
import streamlit as st
import pandas as pd
st.title("M/G/C queuing Model")
def MGC(Arrival_Mean,Service_Mean,No_of_server,ArrivalVariance,ServiceVariance):
    lembda=1/Arrival_Mean
    meu=1/Service_Mean
    c=No_of_server
    p=lembda/(c*meu)
    Ca=ArrivalVariance/((1/lembda)**2)
    Cs=ServiceVariance/((1/meu)**2)
    value=0
    for m in range(c):
        value=value+(((c*p)**m)/(math.factorial(m)))+(((c*p)**c)/(math.factorial(c)*(1-p)))
    Pnot=1/value
    Lq=(Pnot*p*(lembda/meu)**c)/(math.factorial(c)*((1-p)**2))
    Wq=Lq/lembda
    Wq=Wq*((Ca+Cs)/2)
    Lq=lembda*Wq
    Ws=Wq+(1/meu)
    Ls=Ws*lembda
    return Lq,Wq,Ws,Ls,Pnot
Arrival_Mean=st.number_input("Mean arrival rate",step=1.,format="%.2f")
Service_Mean=st.number_input("Mean service rate",step=1.,format="%.2f")
No_of_server=st.number_input('number of servers', 1, 50)
ArrivalVariance=st.number_input('arrival variance', 1, 100)
ServiceVariance=st.number_input('service variance', 1, 100)
Lq,Wq,Ws,Ls,Pnot=MGC(Arrival_Mean,Service_Mean,No_of_server,ArrivalVariance,ServiceVariance)
st.write("wq=",Wq)
st.write("ws=",Ws)
st.write("p=",Pnot)
st.write("lq=",Lq)
st.write("ls=",Ls)