#!/usr/bin/env python
# coding: utf-8

# # Proceso de Wiener n-dimensional
# **Simule una trayectoria del proceso de Wiener vectorial**

# In[98]:


import numpy as np
import matplotlib.pyplot as plt


# In[99]:


from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")


# In[100]:



# Función para simular el proceso de Wiener
def Wiener(n,m,t):
    dt = t/n
    dx = np.power(dt,1/2)
    Wt = np.zeros(((n*t),m))
    for j in range(m):
        for i in range((n*t)-1):
            Wt[0,:] = 0
            Wt[(i+1),j]= Wt[i,j]+ dx*np.random.normal(0,1,1)
    return Wt


# 1. $W(t)=\left(W_1 (t),W_2 (t)\right)$ 

# In[101]:


# Valores
n = 10000
m = 3
t = 1
Wt = Wiener(n,m,t)
plt.plot(Wt[:,0],Wt[:,1],color='darkred',linewidth=1,linestyle='-',label='Wt')
plt.xlabel('W1(t)'); plt.ylabel('W2(t)')
plt.title('Simulación del proceso de wiener en 2 dimensiones')
plt.show()


# 2. $W(t)=\left(W_1 (t),W_2 (t), W_3 (t)\right)$ 

# In[102]:


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# In[105]:


df = pd.DataFrame(Wt,columns =['W1(t)','W2(t)','W3(t)'])
fig = px.line_3d(df, x='W1(t)', y='W2(t)', z='W3(t)')
fig


# In[ ]:




