import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 3em;
            color: #1f77b4;
            margin-bottom: 10px;
        }
        .welcome-text {
            text-align: center;
            font-size: 1.2em;
            color: #555;
            margin-bottom: 30px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Display title and welcome message
st.markdown('<div class="main-title">🌍 World Cities</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-text">Explore cities around the world</div>', unsafe_allow_html=True)

# Add some spacing
st.write("")
st.write("")

# Display welcome content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.info("""
    Welcome to the World Cities app! 🌟
    
    This application provides information and insights about cities across the globe.
    Click the button below to explore the cities database.
    """)
    
    st.write("")
    
    # Button to navigate to app.py
    if st.button("📍 Go to Cities Explorer", use_container_width=True, key="nav_button"):
        st.switch_page("pages/app.py")

# Add footer
st.divider()
st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.9em; margin-top: 50px;">
        🌐 Explore the World • Discover Cities • Learn Cultures
    </div>
""", unsafe_allow_html=True)
