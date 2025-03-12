import re
import streamlit as st

st.set_page_config(page_title="Password Strenth Meter", page_icons="🔑", layout="centered")

st.markdown("""
<style>
            .main {text-align: center;}
            .stTextInput {width: 60% !import; margin: auto; }
            .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px;}
            .stButton button:hover {back-ground: #45a049;}
  </style>          
""", unsafe_allow_html=True)
            
st.title("Password Strength Meter") 
st.write("Enter your password below to Check its security level.🔎")

#function to check password
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ password should be **atleast 8 character long**.")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Password should include **both upper case (A-Z) lower case letters**.")

            if re.search(r"/d", password):
                score += 1
            else:
                feedback.append(" ❌ Password should include **at least one number (0-9) **.")

                #special characters
                if re.search(r"[!@#$%^&*]", password):
                    score += 1
                else:
                    feedback.append(" Include **at least one special character (!@#$%^&*)**.")

                    #results
                    if score == 4:
                        st.successs(" 🔑 **Strong Password**- Your password is secure.")
                    elif score == 3:
                        st.info(" ⚠️ **Moderate Password**  - Consider improving security y adding more feature")
                    else:
                        st.error(" ❌ **Week Password** - Follow the suggestion below to strength it.")

                        #feedback
                        if feedback:
                            with st.expander(" 🔎 **Improve Your password** "):
                                for item in feedback:
                                    st.write(item)
                                    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong  🔒")                         
                    #Button
                    if st.button("Check Strength"):
                        if password:
                                check_password_strength(password)
                    else:
                            st.warning("⚠️ Please enter a password first!")
          