import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("debloated_powerlifting.csv")

# Filter by equipment type
raw_df = df[df["Equipment"] == "Raw"]
sp_df = df[df["Equipment"] == "Single-ply"]
mp_df = df[df["Equipment"] == "Multi-ply"]
wr_df = df[df["Equipment"] == "Wraps"]  # ✅ Fixed here

# Helper: split by sex
def split_by_sex(data):
    return data[data["Sex"] == "M"], data[data["Sex"] == "F"]

# Split datasets
men_df, women_df = split_by_sex(raw_df)
men_df_sp, women_df_sp = split_by_sex(sp_df)
men_df_mp, women_df_mp = split_by_sex(mp_df)
men_df_wr, women_df_wr = split_by_sex(wr_df)

# Grouping function
def prepare_avg_lift_data(data):
    df_clean = data[["BodyweightKg", "TotalKg"]].dropna()
    df_clean["BodyweightKg"] = df_clean["BodyweightKg"].round()
    avg_lifts = df_clean.groupby("BodyweightKg").mean().reset_index()
    return avg_lifts

# Prepare all averages
avg_men = prepare_avg_lift_data(men_df)
avg_women = prepare_avg_lift_data(women_df)
avg_men_sp = prepare_avg_lift_data(men_df_sp)
avg_women_sp = prepare_avg_lift_data(women_df_sp)
avg_men_mp = prepare_avg_lift_data(men_df_mp)
avg_women_mp = prepare_avg_lift_data(women_df_mp)
avg_men_wr = prepare_avg_lift_data(men_df_wr)
avg_women_wr = prepare_avg_lift_data(women_df_wr)

# UI begins
st.title("Powerlifting")

st.write("## What is Powerlifting?")
st.write(
    "Powerlifting is a strength sport that focuses on three main barbell lifts: the squat, bench press, and deadlift. "
    "The goal is to lift the maximum weight for one repetition in each. Competitors aim to build raw strength, discipline, "
    "and consistent technique to maximize performance across these lifts."
)

st.write("## Bodyweight vs Strength (Average Total Lift per Bodyweight)")

# Display section-wise charts
def display_section(title, avg_men, avg_women):
    st.write(f"### {title}")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Men")
        chart_data_men = avg_men.set_index("BodyweightKg")
        st.line_chart(data=chart_data_men, x_label="Bodyweight", y_label="Total")
    with c2:
        st.subheader("Women")
        chart_data_women = avg_women.set_index("BodyweightKg")
        st.line_chart(data=chart_data_women, x_label="Bodyweight", y_label="Total")
# Show each group
display_section("Raw Competitors", avg_men, avg_women)
display_section("Single-Ply Competitors", avg_men_sp, avg_women_sp)
display_section("Multi-Ply Competitors", avg_men_mp, avg_women_mp)
display_section("Wraps Competitors", avg_men_wr, avg_women_wr)
