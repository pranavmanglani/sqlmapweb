import streamlit as st
import subprocess
import os

st.set_page_config(page_title="🧠 SQLMap Web GUI", layout="centered")
st.title("🛡️ SQLMap - Streamlit Wrapper")

# Inputs
target = st.text_input("🎯 Target URL (e.g., http://testphp.vulnweb.com)")
risk = st.selectbox("⚙️ Risk Level", options=[1, 2, 3], index=0)
level = st.selectbox("📊 Test Level", options=[1, 2, 3, 4, 5], index=1)

if st.button("Start Scan"):
    if not target:
        st.error("Please provide a target URL.")
    else:
        st.info("Starting SQLMap scan...")
        cmd = [
            "python3", "sqlmap/sqlmap.py",
            "-u", target,
            "--risk", str(risk),
            "--level", str(level),
            "--batch"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            st.code(result.stdout + result.stderr, language='bash')
        except Exception as e:
            st.error(f"Error running scan: {e}")
