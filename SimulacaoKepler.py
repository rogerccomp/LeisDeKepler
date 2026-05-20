import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados da órbita elíptica
a = 5  # semi-eixo maior
b = 3  # semi-eixo menor

# Distância do centro ao foco
c = np.sqrt(a**2 - b**2)

# O Sol fica em um dos focos da elipse
sol_x = -c
sol_y = 0

# Para simplificar a Terceira Lei de Kepler(k = 1):
# T^2 = k*a^3
k = 3 # constante de proporcionalidade
T = np.sqrt(a**3/k)

# Razão da Terceira Lei de Kepler
razao_kepler = a**3 / T**2

print("Semieixo maior a:", a)
print("Semieixo menor b:", b)
print("Período de translação T:", T)
print("Razão a^3/T^2:", razao_kepler)

# Configuração da simulação
n_frames = 300
tempo = np.linspace(0, T, n_frames)

omega = 2 * np.pi / T
theta = omega * tempo

# Posição do planeta na elipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Criando a figura

fig, ax = plt.subplots(figsize=(7, 6),facecolor='lightgray')

plt.get_current_fig_manager().set_window_title("Trabalho da Disciplina Fundamentos de Modelagem Matemática")
plt.get_current_fig_manager().window.wm_iconbitmap("logo-uerj.ico")

ax.set_xlim(-a - 1, a + 1)
ax.set_ylim(-a - 1, a + 1)
ax.set_aspect('equal')

ax.set_title("Simulação da Terceira Lei de Kepler com Órbita Elíptica",fontsize=14, fontweight='bold')
ax.set_xlabel("x")
ax.set_ylabel("y")

# Desenha a órbita eliptica
theta_orbita = np.linspace(0, 2 * np.pi, 400)
orbita_x = a * np.cos(theta_orbita)
orbita_y = b * np.sin(theta_orbita)

ax.plot(orbita_x, orbita_y, 'k--', label="Órbita elíptica")

# Sol em um dos focos
sol, = ax.plot(sol_x, sol_y, 'yo', markersize=20, label="Sol")

# Planeta
planeta, = ax.plot([], [], 'bo', markersize=10, label="Planeta")

# Linha ligando o Sol ao planeta
linha, = ax.plot([], [], 'k-', linewidth=1)

# Texto informativo
texto = ax.text(
    0.02, 0.95,
    "",
    transform=ax.transAxes,
    fontsize=10,
    verticalalignment="top"
)

ax.legend()

# Função de atualizacao

def atualizar(frame):
    planeta.set_data([x[frame]], [y[frame]])
    linha.set_data([sol_x, x[frame]], [sol_y, y[frame]])

    distancia_sol_planeta = np.sqrt((x[frame] - sol_x)**2 + (y[frame] - sol_y)**2)

    texto.set_text(
        f"Semieixo maior a = {a}\n"
        f"Semieixo menor b = {b}\n"
        f"Período T = {T:.2f}\n"
        f"a³/T² = {razao_kepler:.2f}\n"
        f"Distância Sol-planeta = {distancia_sol_planeta:.2f}\n"
        f"Tempo = {tempo[frame]:.2f}"
    )

    return planeta, linha, texto

# Criando a animação

animacao = FuncAnimation(
    fig,
    atualizar,
    frames=n_frames,
    interval=30,
    blit=True
)

plt.show()
