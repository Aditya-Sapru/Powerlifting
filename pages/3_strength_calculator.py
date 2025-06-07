import streamlit as st 

st.title("Strength Calculator")
st.write("This calculator tells you an estimated one rep max based on the maximum number of reps you hit in a certain lift.")

W = st.number_input("Enter the weight done")
R = st.number_input("Enter the number of reps done")

def onerepmax(w,r):
    ans = w*(1+(r/30))
    return ans

if st.button("Calculate 1RM"):
    one_rep_max = onerepmax(W,R)
    st.write(f"Your estimated 1RM is **{one_rep_max}**")