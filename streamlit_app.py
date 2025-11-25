import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ced import simulate_experiments, plot_trayectoria

st.set_page_config(page_title="Caminata Aleatoria 2D", layout="wide")

st.title("Simulación de Caminata Aleatoria en 2D")

with st.sidebar:
    st.header("Parámetros")
    e = st.number_input("Numero de Caminatas", min_value=1, value=5)
    n = st.number_input("Pasos por Caminata", min_value=1, value=50)
    k = st.number_input("Tamaño del Paso", min_value=1, value=1)
    mostrar_trayectorias = st.checkbox("Mostrar todas las trayectorias", value=True)
    mostrar_finales = st.checkbox("Mostrar sólo posiciones finales", value=False)
    ejecutar = st.button("Ejecutar simulación")

if ejecutar:
    df, trayectorias = simulate_experiments(e, n, k)
    st.subheader("Resultados finales")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Distancia Euclidiana Promedio", value=round(df['valor_euclidiano'].mean(), 3))
        st.metric(label="Distancia Máxima", value=round(df['valor_euclidiano'].max(), 3))
        st.metric(label="Distancia Mínima", value=round(df['valor_euclidiano'].min(), 3))
    with col2:
        st.write("Distribución de distancia euclidiana")
        st.bar_chart(df['valor_euclidiano'])

    if mostrar_trayectorias:
        st.subheader("Trayectorias")
        fig, ax = plt.subplots()
        for pos_x, pos_y in trayectorias:
            ax.plot(pos_x, pos_y, alpha=0.6)
            ax.plot(pos_x[0], pos_y[0], marker='s', color='green')
            ax.plot(pos_x[-1], pos_y[-1], marker='X', color='red')
        ax.set_title("Trayectorias de Caminata Aleatoria 2D")
        st.pyplot(fig)

    if mostrar_finales:
        st.subheader("Posiciones Finales (Scatter)")
        finales_df = pd.DataFrame({"x": df["posicion_final_x"], "y": df["posicion_final_y"], "distancia": df["valor_euclidiano"]})
        st.scatter_chart(finales_df, x="x", y="y")

    st.success("Simulación completada")
else:
    st.info("Configure los parámetros y presione 'Ejecutar simulación'.")
