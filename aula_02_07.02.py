import pandas as pd 
import numpy as np

titanic_csv = 'BASES/Titanic.csv'

df_tarifas = pd.read_csv(titanic_csv, sep=';', encoding='ISO- 8859-1')

print(df_tarifas.head())

("\n ---- TITANIC ----")

array_tarifa = np.array(df_tarifas['Fare'])
array_tarifa_mediana = np.array(df_tarifas['Fare'])


("\n ---- MÉDIA TARIFA PAGAS TITANIC ----")
media_tarifa = np.mean(array_tarifa)
print(f"A média da tarifa do titanic é de:{media_tarifa:.2f}")

("\n ---- MEDIANA DAS TARIFAS PAGAS TITANIC ----")
mediana_tarifa = np.median(array_tarifa_mediana)
print(f"A mediana da tarifa do titanic é de:{mediana_tarifa:.2f}")