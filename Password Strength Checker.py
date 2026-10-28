import streamlit as st
import re

# Set page title and layout
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

st.title(" Password Strength Checker")
st.markdown("Evaluate the security of your password and get real-time feedback on how to improve it.")

password = st.text_input(
    label="Enter your password:", 
    type="password", 
    placeholder="Type a secure password..."
)

score = 0
feedback = []

# Perform checks if input is provided
if password:
    # 3. Check length (Criteria: >= 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # 4. Check uppercase letter
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 5. Check lowercase letter
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 6. Check number
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one numeric digit (0-9).")

    # 7. Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., ! @ # $ %).")

    # 8 & 9. Calculate strength and display results (Weak, Moderate, Strong)
    st.markdown("---")
    st.subheader("Password Strength Analysis")

    if score <= 2:
        st.error("❌ Password Strength: **Weak**")
    elif score <= 4:
        st.warning("Password Strength: **Moderate**")
    else:
        st.success("Password Strength: **Strong**")

    # 10. Display appropriate suggestions for improving a weak/moderate password
    if score < 5:
        st.markdown("### Suggestions to improve your password:")
        for item in feedback:
            st.write(item)
    else:
        st.balloons()
        st.markdown("**Great job! Your password meets all security criteria.**")
else:
    st.info("Please enter a password above to begin analysis.")
