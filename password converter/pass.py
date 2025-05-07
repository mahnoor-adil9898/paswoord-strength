import streamlit as st
import re
st.set_page_config("password strength checker",page_icon="🔒")
st.title("🔒password strength checker")
st.markdown("""## welcome to password strength checker .
use this simple to checkk tour password strength. we wil give helpful tips to create **strong password**""")
password= st.text_input("enter your password" ,type="password")
feedback = []
score = 0
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("password should be at least 8 characters long.")
    if re.search(r'[A-z]', password) and re.search('[a-z]', password):
            score += 1
    else:
         feedback.append("password should contain upper case and lower case.")
    if re.search(r'123', password):
         score += 1
    else:
         feedback.append("password should contain at least one  digit.")
    if re.search(r'[@!&^%$]', password):
         score += 1
    else:
         feedback.append("password should contain at least one special character(@!&^%$).")
    if score == 4:
          feedback.append("password is strong✔")
    elif score==3:
     feedback.append("password is medium ")
    else:
     feedback.append("password is weak make it stronger.")
    if feedback:
          st.markdown("## improvement suggestions")
          for tip in feedback:
               st.write(tip)
else:
     st.info("please enter your password to get started")







