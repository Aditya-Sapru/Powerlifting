import streamlit as st

# Page configuration
st.set_page_config(page_title="Powerlifting: The Big Three", layout="wide")

# Title
st.title("Powerlifting's Big Three Lifts")

st.markdown("""
Powerlifting revolves around three primary lifts that test an athlete's **absolute strength**. 
Each lift is performed under strict rules and contributes to the lifter’s total score in competition.
""")

st.divider()

# Squat Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image("squats_pic.PNG", caption="The Squat", use_container_width=True)
with col2:
    st.subheader("1. Squat")
    st.markdown("""
    The **squat** is the first lift performed in a powerlifting meet. It involves placing a loaded barbell across the upper back (or front of the shoulders) and squatting down to at least **parallel depth** before standing back up.

    - Tests lower body strength (quads, hamstrings, glutes).
    - Requires strong bracing and balance.
    - Red lights are given if the lifter doesn’t reach depth or racks early.
    """)

st.divider()

# Bench Press Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image("Benchpress_pic.PNG", caption="The Bench Press", use_container_width=True)
with col2:
    st.subheader("2. Bench Press")
    st.markdown("""
    The **bench press** is the second lift. The athlete lies flat on a bench, lowers the barbell to their chest, **pauses**, and then presses it back up to full lockout.

    - Tests upper body pushing strength (chest, shoulders, triceps).
    - Requires control, pause, and lockout.
    - Red lights for heaving, uneven lockout, or missed pause.
    """)

st.divider()

# Deadlift Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image("Deadlift_pic.PNG", caption="The Deadlift", use_container_width=True)
with col2:
    st.subheader("3. Deadlift")
    st.markdown("""
    The **deadlift** is the final lift and often the most dramatic. The barbell starts on the floor, and the lifter must pull it to a **fully upright position** with locked knees and hips.

    - Tests full-body strength (back, legs, grip).
    - Variants include sumo and conventional stance.
    - Red lights for hitching, ramping, or not locking out.
    """)

st.divider()

st.markdown("""
### 💡 Summary

| Lift         | Primary Muscles Used         | Key Cues                          |
|--------------|------------------------------|------------------------------------|
| Squat        | Quads, Glutes, Hamstrings    | Depth, Bracing, Upright Chest     |
| Bench Press  | Chest, Triceps, Shoulders    | Pause, Tight Setup, Elbow Tuck    |
| Deadlift     | Back, Glutes, Hamstrings     | Lockout, No Hitch, Grip Strength  |

""")
