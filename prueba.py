import matplotlib.pyplot as plt
import numpy as np

# Datos
h0 = 0.5  # Espesor inicial en mm
modulo_elastico = 6  # MPa
compresibilidad = 0.16  # 16%
max_deformacion = compresibilidad * h0  # Deformación máxima en mm
max_presion = (max_deformacion / h0) * modulo_elastico  # Presión máxima en MPa

# Valores de presión y cierre
presion = np.linspace(0, max_presion, 100)
cierre = (presion / modulo_elastico) * h0
cierre[cierre > max_deformacion] = max_deformacion  # Limitar al cierre máximo

# Gráfico
plt.figure(figsize=(8, 6))
plt.plot(presion, cierre, label="EPDM 0.5 mm")
plt.axhline(y=max_deformacion, color='r', linestyle='--', label="Máx. cierre (16%)")
plt.axvline(x=max_presion, color='g', linestyle='--', label="Máx. presión (0.96 MPa)")
plt.xlabel("Gasket Pressure [MPa]")
plt.ylabel("Closure [mm]")
plt.title("Closure vs Gasket Pressure para junta EPDM")
plt.legend()
plt.grid()
plt.show()