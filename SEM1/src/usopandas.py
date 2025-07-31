import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('./data/datos1.csv')

# # 1. Mostrar datos completos
# print("Datos aerodinámicos completos:")
# print(df)
# #Grafica cl vs alpha
# plt.figure(figsize=(6, 4)) #creo un lienzo de cierto tamaño
# plt.plot(df['alpha'], df['CL'], marker='o', color='blue') #saco los puntos a marcar 
# plt.title("Coeficiente de Sustentación (Cl) vs Ángulo de Ataque") #le doy titulo 
# plt.xlabel("Ángulo de Ataque (°)")
# plt.ylabel("Coeficiente Cl")
# plt.grid(True)
# plt.tight_layout() #lo ajusto para que este bien 
# plt.savefig("./figures/cl_vs_alpha.png")  # Guarda la imagen
# plt.show()

# #Grafica Cd vs alpha 
# plt.figure(figsize=(6, 4))
# plt.plot(df['alpha'], df['CD'], marker='s', color='red')
# plt.title("Coeficiente de Resistencia (Cd) vs Ángulo de Ataque")
# plt.xlabel("Ángulo de Ataque (°)")
# plt.ylabel("Coeficiente Cd")
# plt.grid(True)
# plt.tight_layout()
# plt.savefig("./figures/cd_vs_alpha.png")
# plt.show()
  
# #Cl vs Cd            #Cl fuerza accia arriba que genera ela la Cd, reisitencia al aire (postiivo siempre el aire frena, a mas cd mas energia para moverse)
# plt.figure(figsize=(6, 4))
# plt.plot(df['CD'], df['CL'], marker='^', color='green')
# plt.title("Diagrama Polar: Cl vs Cd")
# plt.xlabel("Cd")
# plt.ylabel("Cl")
# plt.grid(True)
# plt.tight_layout()
# plt.savefig("./figures/cl_vs_cd.png") #./ en el mismo archivo ../ un nuvel mas arriba ../../ dos niveles mas arriba 
# plt.show()

# #Eficniencia aerodinamica cl/cd #es la relacion entre sustentacon y arrastre 
# #calcula al eficiencia si es de cl=1 cd=0.02 la ef=50 --> por cada 1 cd generas 50 de sustentacion 
# df['Eficiencia'] = df['CL'] / df['CD']  #Creo columna donde alamceono los datos 
# max_index = df['Eficiencia'].idxmax() #encuentor el maximo en la columna (indice es numeor de fila), y guuardo el indice en el max indeex
# print("\nÁngulo de máxima eficiencia aerodinámica:")
# print(df.loc[max_index]) #Selecciono toda la fila con el indice entonctrado y saco todos esos valroes 

# #TEORÍA. MAYOR EFICIENCIA= menos combustible= mayor autonomía, quiero mucha sustentación con poco arrastre!!!

# import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 5))
# plt.plot(df['alpha'], df['Eficiencia'], marker='o', label='Cl/Cd')

# # Punto de máxima eficiencia
# plt.scatter(df.loc[max_index, 'alpha'], df.loc[max_index, 'Eficiencia'], color='red', label='Máxima eficiencia')
# plt.text(df.loc[max_index, 'alpha'], df.loc[max_index, 'Eficiencia'] + 0.1,
#          f"{df.loc[max_index, 'Eficiencia']:.2f}", color='red')

# plt.xlabel("Ángulo de ataque (°)")
# plt.ylabel("Cl / Cd")
# plt.title("Eficiencia aerodinámica vs Ángulo de ataque")
# plt.grid(True)
# plt.legend()
# plt.savefig("figures/eficiencia.png")
# plt.show()

#hacemos una funcion que nos de la eficiencia maxima, para cualquier csv dado 
def encontrar_eficiencia_optima(df): #dataframe de pandas,es decir mi csv con la solumas de cl cd ...., es el df=pd.read_csv(...)
    df['Eficiencia'] = df['CL'] / df['CD']
    idx_max = df['Eficiencia'].idxmax() #saco el mayore indice y lo guardo en el idx max 
    return df.loc[idx_max] #el .loc es decirle que me de la fila con el indice x

resultado= encontrar_eficiencia_optima(df)
print("Punto de maxima eficiencia es:", resultado)

#Solo me devuelve el angulo de aatque y la eficicenica
def eficiencia_y_angulo_optimo(df):
    df['Eficiencia'] = df['CL'] / df['CD']
    idx_max = df['Eficiencia'].idxmax()
    angulo_optimo = df.loc[idx_max, 'alpha']
    eficiencia_maxima = df.loc[idx_max, 'Eficiencia']
    return angulo_optimo, eficiencia_maxima

resultado2= eficiencia_y_angulo_optimo(df)
print("REsultado elegido:", resultado2)