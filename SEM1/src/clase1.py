import numpy as np

# Ejemplo: el flujo viene a 50 m/s con un ángulo de 5°
V = 50
alpha_deg = 5
alpha_rad = np.deg2rad(alpha_deg) #paso a radianes ya que el funcioens coseno erc.. cogen en radianes 

# Descomponer velocidad en x e y
Vx = V * np.cos(alpha_rad)
Vy = V * np.sin(alpha_rad)

print(f"Componente Vx: {Vx:.2f} m/s") #son stirngs, : abres .2 son dos deciamens y la "f" es para que sea float (deciamles)
print(f"Componente Vy: {Vy:.2f} m/s")
#con 15 grados 

alpha=10
alpha_rad=np.deg2rad(alpha) 
Vx=V*np.cos(alpha_rad)  #descompongo en x y en y 
Vy=V*np.sin(alpha_rad)

print(f"Componente Vx: {Vx:.2f} m/s")
print(f"Componente Vy: {Vy:.2f} m/s")

#############################################################################################################
#GRAFICO RESULTADOS
import matplotlib.pyplot as plt

# Datos ficticios de un perfil alar
alpha = np.array([-5, 0, 5, 10, 15])
Cl = np.array([-0.4, 0.0, 0.6, 1.2, 1.0])

plt.figure()
plt.plot(alpha, Cl, marker='o') #el marker es para marcar los puntos donde se cogend datos xy
plt.xlabel("Ángulo de ataque (°)")
plt.ylabel("Coef. de sustentación Cl")
plt.title("Perfil NACA2412 - Cl vs α")
plt.axhline(0, color='gray', linestyle='--')
plt.grid(True)
plt.savefig("polar_NACA2412.png") #guarda la imagen  #lo pongo antes para que pueda gardar antes del show
plt.show()



