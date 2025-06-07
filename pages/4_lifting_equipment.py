import streamlit as st

st.set_page_config(page_title="Powerlifting Equipment Guide", layout="wide")

st.title("Powerlifting Equipment Guide")
st.write("Comprehensive guide to powerlifting equipment and their specific uses in training and competition.")

# Main equipment categories
st.header("Equipment Categories")

# Belts
st.subheader("Lifting Belts")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    **Purpose:** Increase intra-abdominal pressure to stabilize the spine during heavy lifts.
    
    **Types:**
    - **Powerlifting Belt (13mm):** Thick, uniform width belt for maximum support
    - **Tapered Belt:** Wider at back, narrower at front for comfort
    - **Lever Belt:** Quick-release mechanism for consistent tightness
    - **Prong Belt:** Traditional buckle system with adjustable tightness
    
    **When to Use:** Heavy sets (80%+ 1RM), working sets in squat and deadlift
    """)
with col2:
    st.info("**Competition Legal**\n- Max width: 10cm\n- Max thickness: 13mm\n- Single prong or lever")

# Wraps and Sleeves
st.subheader("Knee Support")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    **Knee Wraps:**
    - Elastic wraps providing significant assistance
    - Can add 20-50+ lbs to squat
    - Require technique to wrap properly
    - Used in equipped powerlifting divisions
    """)
with col2:
    st.write("""
    **Knee Sleeves:**
    - Neoprene sleeves for warmth and mild support
    - Minimal assistance (~5-10 lbs)
    - Easier to use than wraps
    - Allowed in raw powerlifting divisions
    """)

# Wrist Support
st.subheader("Wrist Support")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    **Wrist Wraps:**
    - Elastic wraps for wrist stability
    - Essential for heavy bench press
    - Various stiffness levels available
    - Length: 12-36 inches (competition max: 1m)
    """)
with col2:
    st.write("""
    **Wrist Straps:**
    - Leather/fabric straps for grip assistance
    - Used in training for deadlifts and rows
    - **NOT allowed in powerlifting competition**
    - Help overcome grip limitations
    """)

# Suits and Shirts
st.subheader("Supportive Gear (Equipped Division)")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    **Squat Suits:**
    - Tight-fitting canvas/denim suits
    - Provide significant assistance out of the hole
    - Can add 100+ lbs to squat
    - Require specific technique
    """)
with col2:
    st.write("""
    **Bench Shirts:**
    - Extremely tight polyester/canvas shirts
    - Provide assistance at chest level
    - Can add 50-200+ lbs to bench
    - Very technical to use effectively
    """)

# Shoes
st.subheader("Footwear")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("""
    **Squat Shoes:**
    - Raised heel (0.5-1.5")
    - Solid, non-compressible sole
    - Improves ankle mobility
    - Better upright posture
    """)
with col2:
    st.write("""
    **Deadlift Shoes:**
    - Flat, thin sole
    - Minimal heel-to-toe drop
    - Reduces bar travel distance
    - Better ground connection
    """)
with col3:
    st.write("""
    **Chuck Taylors:**
    - Flat, stable platform
    - Good all-around option
    - Suitable for all three lifts
    - Popular competition choice
    """)

# Accessories
st.subheader("Training Accessories")

accessories = {
    "Chalk": "Improves grip by absorbing moisture. Essential for heavy deadlifts.",
    "Resistance Bands": "Variable resistance for speed work and accommodating resistance.",
    "Chains": "Accommodating resistance that increases load at lockout.",
    "Safety Bars": "Specialized barbells (SSB, trap bar) for variation and injury prevention.",
    "Blocks/Pins": "For partial range of motion training and overload work.",
    "Slingshot": "Bench press assistance tool for overload and technique work."
}

for item, description in accessories.items():
    st.write(f"**{item}:** {description}")

# Competition Rules
st.header("Competition Equipment Rules")

st.subheader("Raw Division (IPF Rules)")
raw_allowed = [
    "Belt (max 10cm wide, 13mm thick)",
    "Wrist wraps (max 1m long)",
    "Knee sleeves (max 30cm long, 7mm thick)",
    "Singlet",
    "T-shirt (bench press)",
    "Socks",
    "Shoes"
]

st.subheader("Equipped Division")
equipped_additional = [
    "Squat suit (single or multi-ply)",
    "Bench shirt (single or multi-ply)",
    "Knee wraps (max 2.5m long)",
    "Deadlift suit"
]

col1, col2 = st.columns(2)
with col1:
    st.write("**Raw Division Allowed:**")
    for item in raw_allowed:
        st.write(f"• {item}")

with col2:
    st.write("**Additional Equipped Items:**")
    for item in equipped_additional:
        st.write(f"• {item}")

# Equipment Selection Guide
st.header("Equipment Selection Guide")

st.subheader("Beginner Priority")
beginner_order = [
    "Proper shoes (flat sole or squat shoes)",
    "Lifting belt (13mm leather)",
    "Wrist wraps (medium stiffness)",
    "Knee sleeves (if needed)",
    "Chalk"
]

st.subheader("Advanced Additions")
advanced_order = [
    "Specialized shoes for each lift",
    "Competition-grade belt",
    "Multiple wrist wrap stiffnesses",
    "Training accessories (bands, chains)",
    "Backup equipment"
]

col1, col2 = st.columns(2)
with col1:
    st.write("**Start with these essentials:**")
    for i, item in enumerate(beginner_order, 1):
        st.write(f"{i}. {item}")

with col2:
    st.write("**Add these as you progress:**")
    for i, item in enumerate(advanced_order, 1):
        st.write(f"{i}. {item}")

# Cost Considerations
st.header("💰 Budget Considerations")

budget_tiers = {
    "Budget Starter Kit ($100-200)": [
        "Basic leather belt",
        "Canvas shoes (Chucks)",
        "Basic wrist wraps",
        "Chalk"
    ],
    "Intermediate Setup ($300-500)": [
        "Quality 13mm belt",
        "Squat shoes",
        "Competition wrist wraps",
        "Knee sleeves",
        "Deadlift slippers"
    ],
    "Advanced/Competition ($500+)": [
        "Premium belt (Inzer, SBD)",
        "Multiple shoe options",
        "Various wrap stiffnesses",
        "Backup equipment",
        "Specialized accessories"
    ]
}

for tier, items in budget_tiers.items():
    with st.expander(tier):
        for item in items:
            st.write(f"• {item}")

# Maintenance Tips
st.header("Equipment Maintenance")

maintenance_tips = {
    "Belts": "Clean with leather conditioner, store flat, avoid excessive moisture",
    "Wraps": "Hand wash, air dry, avoid fabric softener",
    "Sleeves": "Wash inside-out, air dry, use sleeve-specific detergent",
    "Shoes": "Rotate pairs, clean soles, store in dry environment"
}

for equipment, tip in maintenance_tips.items():
    st.write(f"**{equipment}:** {tip}")

st.info("**Pro Tip:** Invest in quality equipment gradually. Start with essentials and upgrade as your lifting progresses and you understand your specific needs.")