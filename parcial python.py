#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd # importat la libreria pandas como pd
import numpy as np 
import matplotlib.pyplot as plt


# In[2]:


datos =pd.read_csv("accidentes-envigado.csv") # cargar desde jupyter el archivo accidentes-envigado.cvs


# In[24]:


datos.columns # Mostrar


# In[25]:


datos.head() #Mostrar cabecera


# In[26]:


datos.info()#Mostrar datos de la tabla


# In[27]:


datos #Mostrar todo los datos de la tabla "Consulta 2"


# In[ ]:





# In[30]:


datos[["CLASE DE VEHICULO","GRAVEDAD"]]#Consulta de datos con variables 3


# In[38]:


datos.iloc[[4,9],]#Consulta de datos especificos


# In[41]:


datos = datos.dropna(subset=["Coordenadas"])


# In[20]:


nuevos_datos = datos.dropna() 


# In[17]:


datos.SEXO.describe()


# In[18]:


datos.describe()


# In[21]:


nuevos_datos


# In[44]:


nuevos_datos.reset_index().to_csv("nuevos_datos.csv",header=True,index=False)# creacion de un nuevo archivo en formato .csv en nuevo dato.


# In[45]:


nuevos_datos


# In[ ]:




