# Project 2 Password Strength Meter 

import re 
import streamlit as st 

# page styling 
st.set_page_config(page_title="Password Strenghth Checker By Alishba", page_icon="🗝️",layout="centered")

# custom css 
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important;}
    .stButton button {width: 60%;  background-color:black; color:white; font-size: 18px; }
    .stButton button:hover { background-color:#A9A9A9; color:black; }
</style>
""", unsafe_allow_html=True)


# page title and description 
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level.🔍")

# check the function to strength password 
def check_password_strength(password):
    score = 0
     feedback = []

    if len (password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Password should be *at least 8 characters long*.")
    
    if re.search(r"[A-Z]", password ) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should be include *both uppercase (A-Z) and lowercase (a-z) letters*.")

    if re.search (r"\d",password):
        score += 1
    else:
        feedback.append("❌ Password should be include *at least one number (0-9)*.")

#  special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&)**.")


    # display the password strength result 
    if score == 4:
        st.success("✅ *Strong Password* Your password is secure.")
    elif score == 3 :
        st.info("⚠️*Moderate Password* - Consider improving security by adding more feature.")
    else:
        st.error("❌ *Week Password* - Follow the suggestion below to strength it.")

    
    # feedback outuput 
    if feedback:
        with st.expander("🔍*Improve Your Password*"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")


# working of button 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!") # show warning if password is empty
           
   
    
   
    
           

              
                     
