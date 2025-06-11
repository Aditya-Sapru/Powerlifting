# Powerlifting Analytics Dashboard

A comprehensive Streamlit web application for powerlifting enthusiasts, providing educational content about supportive gear, strength curve analysis, and performance calculators.

## Features

### 📚 Educational Content
- **Powerlifting Overview**: Introduction to the sport of powerlifting
- **Supportive Gear Guide**: Comprehensive information about powerlifting supportive equipment including:
  - Lifting belts (leather vs. nylon, width specifications)
  - Knee wraps vs. knee sleeves
  - Wrist wraps and straps
  - Lifting suits (single-ply vs. multi-ply)
  - Competition regulations and equipment categories

### 📊 Data Visualization
- **Strength Curves Analysis**: Interactive graphs showing bodyweight vs. total weight relationships across different equipment categories:
  - **Raw Division**: No supportive equipment
  - **Single-Ply**: Single-layer supportive suits
  - **Multi-Ply**: Multi-layer supportive suits  
  - **Wraps Division**: Knee wraps allowed
  - **Gender Differentiation**: Separate curves for male and female lifters

### 🧮 Calculators
- **DOTS Calculator**: Calculate your DOTS score for competition comparison across weight classes
- **1RM Calculator**: Estimate your one-rep maximum using the Epley formula based on submaximal lifts


## Usage

### DOTS Calculator
1. Navigate to the DOTS Calculator section
2. Enter your:
   - Body weight (kg)
   - Competition lifts (Squat, Bench Press, Deadlift)
3. View your DOTS score and percentile ranking

### 1RM Calculator
1. Go to the 1RM Calculator section
2.  Input your weight lifted and repetitions performed
3. View your estimated 1RM using the Epley formula
4. Use results for training programming and goal setting

### Strength Curve Analysis
- Explore interactive charts showing bodyweight vs. total weight relationships
- Toggle between equipment divisions:
  - Raw (no supportive gear)
  - Single-Ply (single-layer suits)
  - Multi-Ply (multi-layer suits)
  - Wraps (knee wraps allowed)
- View separate curves for male and female lifters
- Identify strength standards across different body weights


## Technical Implementation

### Key Libraries Used
- **Streamlit**: Web app framework
- **Pandas**: Data manipulation and analysis

### Calculator Formulas

**DOTS Score Calculation:**
```
DOTS = Total × (500 / (A × BW² + B × BW + C))
```
Where coefficients A, B, C are gender-specific constants defined by the IPF.

**1RM Formula (Epley):**
```
1RM = weight × (1 + reps/30)
```

### Equipment Categories

**Raw Division:**
- No supportive equipment allowed
- Belt, wrist wraps, and knee sleeves permitted

**Single-Ply Division:**
- Single-layer supportive suits
- Moderate assistance from equipment

**Multi-Ply Division:**
- Multi-layer supportive suits
- Maximum equipment assistance

**Wraps Division:**
- Knee wraps allowed (typically 2.5m length)
- Intermediate support level

## Data Visualization Features

The strength curve graphs display:
- X-axis: Bodyweight (kg)
- Y-axis: Total weight lifted (kg)
- Color coding by equipment division
- Gender-specific trend lines
- Interactive tooltips with lifter details
- Percentile markers for strength standards
