import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
x = np.linspace(-10,10,100)
 
def normal_dist(x , mean , sd):
    prob_density = np.exp(-0.5*((x-mean)/sd)**2) / np.sqrt(np.pi * sd**2)
    return prob_density
 
mean = st.slider(label='input mean', min_value=0., max_value=100., value=4.)
sd = st.slider(label='input std dev', min_value=0.1, max_value=100., value=4.)
 
pdf = normal_dist(x,mean,sd)

fig, ax = plt.subplots()
plt.plot(x, pdf , color = 'blue')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
st.pyplot(fig)
