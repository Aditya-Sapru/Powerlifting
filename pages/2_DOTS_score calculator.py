import streamlit as st

st.title("DOTS Score Calculator")
st.write("DOTS score is used in powerlifting to compare lifters of different bodyweights and genders.")

sex = st.selectbox("Sex", ["M", "F"])
bodyweight = st.number_input("Bodyweight (kg)", min_value=30.0, max_value=200.0, step=0.1)
total = st.number_input("Total Lift (kg)", min_value=50.0, max_value=1200.0, step=1.0)

def calculate_dots(bodyweight, total, sex):
    bw = round(bodyweight, 1)
    
    if sex == 'M':
        a, b, c, d, e = -307.75076, 24.0900756, -0.1918759221, 0.0007391293, -0.000001093492
    elif sex == 'F':
        a, b, c, d, e = -57.96288, 13.6175032, -0.1126655495, 0.0005158568, -0.0000010706
    else:
        return None

    denominator = a + b*bw + c*bw**2 + d*bw**3 + e*bw**4
    if denominator <= 0:
        return None
    return 500 * total / denominator

if st.button("Calculate DOTS"):
    score = calculate_dots(bodyweight, total, sex)
    if score:
        st.success(f"Your DOTS score is: **{score:.2f}**")
    else:
        st.error("Invalid input or division error. Please check your values.")