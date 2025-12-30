import streamlit as st
from engine import SecurityEngine

def page_dashboard(length, u_upper, u_lower, u_digits, u_symbols):
    st.markdown("## Secure Password Generator")
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    
    if st.button("⚡️ Generate New Password", use_container_width=True, type="primary"):
        pwd, ent = SecurityEngine.generate_password(length, u_upper, u_lower, u_digits, u_symbols)
        if pwd:
            st.session_state['result'] = {'pwd': pwd, 'ent': ent}
            st.toast("Generated Successfully!", icon="✅")
        else:
            st.error("Select at least one character type.")

    if 'result' in st.session_state:
        data = st.session_state['result']
        label, color, score = SecurityEngine.get_strength_meta(data['ent'])
        st.markdown(f'<div class="password-box"><div class="password-text">{data["pwd"]}</div></div>', unsafe_allow_html=True)
        st.code(data['pwd'], language="text")
        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Length", len(data['pwd']))
        m2.metric("Entropy", f"{int(data['ent'])} bits")
        m3.metric("Strength", label)
        with m4:
            st.write("Security Score")
            st.progress(score / 100)
    st.markdown('</div>', unsafe_allow_html=True)

def page_api():
    st.markdown("## Developer API")
    st.markdown('<div class="css-card">Integrate security into CI/CD.</div>', unsafe_allow_html=True)

def page_docs():
    st.markdown("## Documentation")
    st.markdown('<div class="css-card">Installation: <code>pip install cipherguard-cli</code></div>', unsafe_allow_html=True)

def page_login():
    st.markdown("## Login")