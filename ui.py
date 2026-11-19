import streamlit as st
import os
import pandas as pd
import plotly.express as px
import librosa

# 1. SETUP & CONFIG
st.set_page_config(layout="wide", page_title="SampleSaber")

# Load the local CSV
df = pd.read_csv('mapped_samples_local.csv')

st.title("🌌 SampleSaber")

# 2. SIDEBAR - THE "ABSYNTH" HIGHLIGHTER
st.sidebar.header("🎯 Focus Mode")
all_folders = df['folder'].unique().tolist()
selected_folders = st.sidebar.multiselect("Highlight Categories", all_folders, default=all_folders)

# Ghosting Logic
df['display_status'] = df['folder'].apply(lambda x: x if x in selected_folders else "Ghosted")

# 3. THE PLOT (Refined Eye-Candy)
fig = px.scatter(
    df, x='x', y='y', 
    color='display_status', 
    hover_name='name',
    template='plotly_dark',
    height=700,
    custom_data=['path', 'name'], 
    color_discrete_map={"Ghosted": "rgba(100, 100, 100, 0.1)"}
)

fig.update_traces(
    marker=dict(size=8, line=dict(width=0.5, color='white'), opacity=0.8),
    selector=dict(mode='markers')
)

fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=""),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, title=""),
    margin=dict(l=0, r=0, t=0, b=0) # Maximizes space
)

# SINGLE CHART CALL
event_data = st.plotly_chart(fig, on_select="rerun", use_container_width=True)

# 4. DYNAMIC PREVIEW PANEL
if event_data and event_data.selection.points:
    # Use custom_data to avoid index shifting bugs
    selected_path = event_data.selection.points[0]['customdata'][0]
    selected_name = event_data.selection.points[0]['customdata'][1]
    
    # Visual Separation
    st.divider()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader(f"🎧 {selected_name}")
        if os.path.exists(selected_path):
            st.audio(selected_path)
        else:
            st.error("File Path Error")

    with col2:
        # Mini Waveform Preview (Fast load)
        try:
            y, sr = librosa.load(selected_path, sr=22050, duration=5.0) # Limit to 5s for speed
            st.line_chart(y[::150], color="#7792E3", height=150)
        except Exception as e:
            st.write("Waveform preview unavailable.")
else:
    st.info("💡 Click a star in the galaxy to preview the sound.")