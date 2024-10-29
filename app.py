import streamlit as st
import numpy as np

def calculate_hba1c(avg_glucose):
    # Formula to estimate HbA1c from average glucose
    # Formula: (Avg Glucose in mg/dL + 46.7) / 28.7
    return (avg_glucose + 46.7) / 28.7

# Main function
def main():
    st.title("Blood Glucose Level Assessment and HbA1c Estimator")
    
    # Input section for blood glucose readings
    st.header("Enter Your Blood Glucose Readings")
    morning_glucose = st.number_input("Morning Blood Glucose (mg/dL)", min_value=0)
    afternoon_glucose = st.number_input("Afternoon Blood Glucose (mg/dL)", min_value=0)
    evening_glucose = st.number_input("Evening Blood Glucose (mg/dL)", min_value=0)
    
    # Average blood glucose calculation
    if morning_glucose and afternoon_glucose and evening_glucose:
        avg_glucose = np.mean([morning_glucose, afternoon_glucose, evening_glucose])
        st.write(f"**Your Average Blood Glucose:** {avg_glucose:.2f} mg/dL")
        
        # Calculate estimated HbA1c
        estimated_hba1c = calculate_hba1c(avg_glucose)
        st.write(f"**Estimated HbA1c:** {estimated_hba1c:.2f}%")
        
        # Health advice based on blood glucose levels
        st.header("Health Advice")
        if avg_glucose < 70:
            st.warning("Your blood glucose level is too low. Please consult a healthcare provider.")
        elif 70 <= avg_glucose <= 140:
            st.success("Your blood glucose level is within the healthy range!")
        elif 140 < avg_glucose <= 180:
            st.info("Your blood glucose level is slightly elevated. Consider lifestyle modifications.")
        else:
            st.error("Your blood glucose level is too high. Consult a healthcare provider.")

if __name__ == "__main__":
    main()
