import streamlit as st 
import pandas as pd 
import altair as alt 
import seaborn as sns
import time 
st.title("Palmer's Penguins")
st.markdown("Use this streamlit app to make your own scatterplot about penguins!")
#1-selected_species = st.selectbox("What species would you like to visualize?",["Adelie","Gentoo","Chinstrap"])

penguin_file = st.file_uploader("Select Your Local Penguin CSV (default provided)")
"""
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()
"""
@st.cache_data
def load_file(penguin_file):
    time.sleep(10)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv(penguin_file)
    return(df)
penguins_df = load_file(penguin_file)
selected_x_var = st.selectbox("What do you want x variable to be?",["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"])
selected_y_var = st.selectbox("What do you want y variable to be?",["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"])
selected_gender = st.selectbox("what gender do you want to filter for?", ["all penguins", "male penguins","female penguins"])

if selected_gender == "male penguins":
    penguins_df = penguins_df[penguins_df['sex']=="male"]
elif selected_gender == "female penguins":
    penguins_df = penguins_df[penguins_df['sex']=="female"]
else:
    pass

#1-penguins_df = penguins_df[penguins_df["species"] == selected_species]
   #sns.set_style("darkgrid")
   #markers = {"Adelie":"X", "Gentoo":"s", "Chinstrap":"o"}
alt_chart = (
    #1-alt.Chart(penguins_df,title=f"Scatterplot of {selected_species} Penguins")
    alt.Chart(penguins_df,title=f"Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",#if you activate 1- cancel this line.
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)


