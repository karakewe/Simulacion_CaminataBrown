import random
import pandas as pd
import matplotlib.pyplot as plt
import time

def evento_50_porciento_random():
    if random.random() < 0.5:
        return "Sí aumenta"
    return "No aumenta"

def euclidiana(x, y):
    return (x**2 + y**2)**0.5

def simulate_random_walk_2d(n_iteraciones, unidad_incremento):
    posicion_x = [0]
    posicion_y = [0]
    for idx in range(n_iteraciones):
        resultado_x = evento_50_porciento_random()
        if resultado_x == "Sí aumenta":
            posicion_x.append(posicion_x[idx] + unidad_incremento)
        else:
            posicion_x.append(posicion_x[idx] - unidad_incremento)
    for idy in range(n_iteraciones):
        resultado_y = evento_50_porciento_random()
        if resultado_y == "Sí aumenta":
            posicion_y.append(posicion_y[idy] + unidad_incremento)
        else:
            posicion_y.append(posicion_y[idy] - unidad_incremento)
    return posicion_x, posicion_y

def simulate_experiments(cantidad_experimentos, n_iteraciones, unidad_incremento):
    df_resultados = pd.DataFrame()
    trayectorias = []
    for _ in range(cantidad_experimentos):
        start = time.time()
        pos_x, pos_y = simulate_random_walk_2d(n_iteraciones, unidad_incremento)
        end = time.time()
        duration = end - start
        dicc = {
            "n_iteraciones": n_iteraciones,
            "posicion_final_x": pos_x[-1],
            "posicion_final_y": pos_y[-1],
            "valor_euclidiano": euclidiana(pos_x[-1], pos_y[-1]),
            "duracion" : duration
        }
        df_resultados = pd.concat([df_resultados, pd.DataFrame([dicc])], ignore_index=True)
        trayectorias.append((pos_x, pos_y))
    return df_resultados, trayectorias

def plot_trayectoria(pos_x, pos_y):
    plt.plot(pos_x, pos_y)
    plt.plot(pos_x[0], pos_y[0], marker='s', color='green', label='Inicio')
    plt.plot(pos_x[-1], pos_y[-1], marker='X', color='red', label='Fin')
    plt.title("Caminata Aleatoria en 2D")
    plt.legend()
    return plt.gcf()

def run_cli():
    e = int(input("Cantidad de Caminatas:"))
    n = int(input("Pasos por Caminata: "))
    k = int(input("Tamaño del Paso: "))
    df, trayectorias = simulate_experiments(e, n, k)
    for pos_x, pos_y in trayectorias:
        plot_trayectoria(pos_x, pos_y)
        plt.show()
    print(df)

if __name__ == "__main__":
    run_cli()
