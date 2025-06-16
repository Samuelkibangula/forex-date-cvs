import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(page_title="Forex IA", layout="wide")
st.title("📈 Mon Assistant Forex Intelligent")

# Chargement des données
df = pd.read_csv("forex_data.csv", parse_dates=['Datetime'])

# Affichage du dernier signal
dernier_signal = df['Signal'].iloc[-1]
couleur = "green" if "ACHETER" in dernier_signal else "red" if "VENDRE" in dernier_signal else "gray"
st.markdown(f"### Dernière recommandation : <span style='color:{couleur}'>{dernier_signal}</span>", 
            unsafe_allow_html=True)

# Graphique interactif
fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=df['Datetime'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name="Prix"
))

fig.update_layout(
    title=f"Analyse de {paire_devise}",
    xaxis_rangeslider_visible=False
)
st.plotly_chart(fig, use_container_width=True)

# Tableau des signaux récents
st.write("### Historique des signaux")
st.dataframe(df[['Datetime', 'Close', 'RSI', 'Signal']].tail(10))
