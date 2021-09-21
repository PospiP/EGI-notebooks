#!/usr/bin/env python
# coding: utf-8

# # **EGI Services**

# [https://www.egi.eu/services/](https://www.egi.eu/services/)

# # **Přihlášení do EGI:**

# 1) Vytvoření EGI účtu
# 2) Přihlášení do vo.notebooks.egi.eu VO
# 3) Příhlášení do EGI notebooks 

# # Může v něm být nadpis - to už víme
# 
# ## a ten se může zmenšovat
# 
# ### a zmenšovat
# 
# #### a zmenšovat
# 
# ##### a zmenšovat
# 
# ###### a zmenšovat, až už ho nikdo nepřečtě

# In[1]:


import sys
print(sys.version)


# In[2]:


from IPython.display import Image


# In[3]:


Image("http://sipi.usc.edu/database/preview/misc/4.2.03.png")


# ## Interactive widgets

# Example that render an interactive widget

# In[4]:


import ipywidgets as ipw


# In[5]:


slider = ipw.IntSlider(min=0, value=10, max=20)
slider


# In[6]:


slider


# In[7]:


import panel as pn
pn.extension()


# In[8]:


def f(x):
    return x


# In[9]:


pn.interact(f, x=10)


# # EGI services

# <img src="pictures/EGI_Services.png"  alt="Drawing" style="width: 1000px"/>

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/datatest.txt')

Dx = data["date"]

data['date'] = data.date.astype('datetime64[ns]')
data = data.set_index('date')

data.tail()


# In[11]:


from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(10,5));
plt.plot(data.CO2);
plt.xticks(rotation=45);
plt.xlabel('Date', fontsize = 20)
plt.ylabel('Temperature',fontsize = 20)

plt.show()


# # Můžu použít nějakou statistiku - třeba rolling mean:

# $$ \tau = \frac{\varpi - \omega}{\sqrt{\frac{\sum \varpi - \omega}{N(N-1)}}} $$

# Tohle sice není rolling mean, ale aspoň vidíte, že se sem dá dát i **LaTeX**

# In[12]:


def mpl_plot(avg, highlight):
    fig = Figure()
    FigureCanvas(fig) 
    ax = fig.add_subplot()
    avg.plot(ax=ax)
    if len(highlight): highlight.plot(style='o', ax=ax)
    return fig

def find_outliers(variable='Temperature', window=50, sigma=10, view_fn=mpl_plot):
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = (np.abs(residual) > std * sigma)
    return view_fn(avg, avg[outliers])


# In[13]:


find_outliers(variable='CO2', window=50, sigma=10)


# In[14]:


import panel as pn
pn.extension()

pn.interact(find_outliers)

