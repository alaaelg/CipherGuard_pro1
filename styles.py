import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* استيراد الخطوط */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Cairo:wght@400;600;700&display=swap');

        /* تعيين الخط العام للتطبيق */
        * { font-family: 'Inter', 'Cairo', sans-serif; }

        /* --- تعديل لون الأزرار إلى الأحمر --- */
        div.stButton > button {
            color: #ffffff !important; /* لون النص أبيض ناصع للوضوح */
            background: linear-gradient(135deg, #ef4444 0%, #991b1b 100%) !important; /* تدرج أحمر احترافي */
            border: none;
            border-radius: 8px;
            font-weight: 700;
            transition: 0.3s;
        }

        /* تغيير بسيط عند الوقوف بالماوس على الزر */
        div.stButton > button:hover {
            background: #b91c1c !important; 
            border: none;
        }

        /* --- ضمان وضوح النصوص الأخرى --- */
        /* نصوص الصفحة الرئيسية */
        [data-testid="stAppViewContainer"] h1, 
        [data-testid="stAppViewContainer"] h2, 
        [data-testid="stAppViewContainer"] h3, 
        [data-testid="stAppViewContainer"] p, 
        [data-testid="stAppViewContainer"] span, 
        [data-testid="stAppViewContainer"] label {
            color: #1e293b !important;
        }

        /* نصوص القائمة الجانبية (الأبيض) */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stMarkdown,
        div[data-testid="stThumbValue"], 
        div[data-testid="stTickBarMin"], 
        div[data-testid="stTickBarMax"] {
            color: #ffffff !important;
        }

        /* كلمة السر */
        .password-text {
            color: #ef4444 !important; /* جعلنا كلمة السر حمراء أيضاً لتتناسق مع الأزرار */
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)