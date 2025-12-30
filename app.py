import streamlit as st
from styles import apply_styles
from components import render_navbar, render_sidebar, render_footer
from pages_content import page_dashboard, page_api, page_docs, page_login

# 1. Page Configuration
st.set_page_config(page_title="CipherGuard", page_icon="🛡", layout="wide")

# 2. Apply Styles
apply_styles()

# 3. State Management
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

# 4. Main Flow
def main():
    render_navbar()
    
    # Sidebar Logic
    if st.session_state.current_page == 'Dashboard':
        params = render_sidebar()
    else:
        st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)
        params = (16, True, True, True, True)

    # Routing
    cp = st.session_state.current_page
    if cp == 'Dashboard': page_dashboard(*params)
    elif cp == 'API': page_api()
    elif cp == 'Docs': page_docs()
    elif cp == 'Login': page_login()

    render_footer()

if __name__ == "__main__":
    main()