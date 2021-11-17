# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
st.title('ATPy Masters Bets')



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importer le fichier Atp_Paris_Master.csv et afficher les variables



df=pd.read_csv(r'C:\Users\Boisse\Desktop\Data Science\Datasets\atp_data.csv')

dftypes=df.dtypes
dfnombreduniques=df.nunique()
noms=df.columns
dfexpli = pd.DataFrame(list(zip(noms,dftypes,dfnombreduniques)), columns = ['Colonnes','Dtypes','Nombre de valeurs uniques'])

dfexpli.sort_values(by = ['Nombre de valeurs uniques']).head(23)
#On constate plusieurs choses :
    #les colonnes de données Float ou Int on toutes de très nombreuses valeurs différentes, ce qui est attendu
    #La plupart des colonnes de type Object et certaines numériques (comme Best Of / Wsets / Lsets) ont peu de valeurs différentes et peuvent être traitées comme des catégorielles
    
    
    
df['Date']=pd.to_datetime(df['Date']) #On utilise DateTime pour pouvoir trier comparer les dates
pd.set_option("max_columns", None) #Pour afficher toutes les colonnes

st.write('Dataframe nettoyé :')
st.write(df)

