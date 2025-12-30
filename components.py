import streamlit as st

def set_page(page_name):
    st.session_state.current_page = page_name

def render_sidebar():
    with st.sidebar:
        st.markdown("### 🛡 CipherGuard")
        st.caption("Enterprise Security Edition v3.0")
        st.markdown("---")
        st.header("⚙️ Configuration")
        length = st.slider("Password Length", 8, 64, 16)
        col1, col2 = st.columns(2)
        with col1:
            u_upper = st.checkbox("A-Z", True)
            u_digits = st.checkbox("0-9", True)
        with col2:
            u_lower = st.checkbox("a-z", True)
            u_symbols = st.checkbox("@#$", True)
        st.markdown("---")
        st.info("💡 Pro Tip: Use phrases combined with symbols for maximum entropy.")
        return length, u_upper, u_lower, u_digits, u_symbols

def render_navbar():
    with st.container():
        c1, c2, c3 = st.columns([1.5, 3, 1])
        with c1:
            st.markdown("<h3 style='margin:0; padding-top:5px; color:#2563eb !important;'>CipherGuard <span style='color:#1e293b; font-size:0.8em'>Pro</span></h3>", unsafe_allow_html=True)
        with c2:
            b1, b2, b3 = st.columns(3)
            with b1:
                if st.button("📊 Dashboard", use_container_width=True): set_page('Dashboard')
            with b2:
                if st.button("🔗 API Access", use_container_width=True): set_page('API')
            with b3:
                if st.button("📄 Docs", use_container_width=True): set_page('Docs')
        with c3:
             if st.button("Login 👤", use_container_width=True): set_page('Login')
        st.markdown("<hr style='margin-top:10px; margin-bottom:20px; border-color:#e2e8f0;'>", unsafe_allow_html=True)

def render_footer():
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #64748b; font-size: 0.9rem; padding-bottom: 20px;'>
            &copy; 2025 CipherGuard Inc. All rights reserved.
        </div>
    """, unsafe_allow_html=True)