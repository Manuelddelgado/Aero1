import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('../data/datos1.csv')

# 1. Mostrar datos completos
print("Datos aerodinámicos completos:")
print(df)
#Grafica cl vs alpha
plt.figure(figsize=(6, 4)) #creo un lienzo de cierto tamaño
plt.plot(df['alpha'], df['CL'], marker='o', color='blue') #saco los puntos a marcar 
plt.title("Coeficiente de Sustentación (Cl) vs Ángulo de Ataque") #le doy titulo 
plt.xlabel("Ángulo de Ataque (°)")
plt.ylabel("Coeficiente Cl")
plt.grid(True)
plt.tight_layout() #lo ajusto para que este bien 
plt.savefig("../data/cl_vs_alpha.png")  # Guarda la imagen
plt.show()

#Grafica Cd vs alpha 
plt.figure(figsize=(6, 4))
plt.plot(df['alpha'], df['CD'], marker='s', color='red')
plt.title("Coeficiente de Resistencia (Cd) vs Ángulo de Ataque")
plt.xlabel("Ángulo de Ataque (°)")
plt.ylabel("Coeficiente Cd")
plt.grid(True)
plt.tight_layout()
plt.savefig("../data/cd_vs_alpha.png")
plt.show()

#Cl vs Cd
plt.figure(figsize=(6, 4))
plt.plot(df['CD'], df['CL'], marker='^', color='green')
plt.title("Diagrama Polar: Cl vs Cd")
plt.xlabel("Cd")
plt.ylabel("Cl")
plt.grid(True)
plt.tight_layout()
plt.savefig("../data/cl_vs_cd.png")
plt.show()

#Eficniencia aerodinamica cl/cd
df['Eficiencia'] = df['CL'] / df['CD']
max_index = df['Eficiencia'].idxmax()
print("\nÁngulo de máxima eficiencia aerodinámica:")
print(df.loc[max_index])

