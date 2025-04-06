import streamlit as st

def load_css():
    """Load custom CSS styles for the application"""
    st.markdown("""
    <style>
        .main {
            background-color: #f8faf9;
            padding-left: 5rem !important;
            padding-right: 5rem !important;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 15px 20px;
            font-weight: bold;
            width: 100%;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .css-18e3th9 {
            padding-top: 1.5rem;
        }
        .css-hxt7ib {
            padding-top: 1.5rem;
        }
        .stTitle {
            color: #2e7d32;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding: 1rem;
            background-color: rgba(76, 175, 80, 0.1);
            border-radius: 10px;
        }
        .extra-menu {
            position: relative;
            display: inline-block;
        }
        .extra-menu-btn {
            background-color: #2e7d32;
            color: white;
            border-radius: 5px;
            padding: 10px 15px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .extra-menu-btn:hover {
            background-color: #1b5e20;
        }
        .card {
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: white;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }
        .stForm {
            padding: 1.5rem;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
        }
        .stTabs [data-baseweb="tab"] {
            height: 3rem;
            border-radius: 5px 5px 0 0;
            padding: 0 1rem;
            font-weight: 500;
        }
        .stChatMessage {
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 10px;
        }
        .streamlit-expanderHeader {
            font-weight: 600;
            background-color: rgba(76, 175, 80, 0.1);
            border-radius: 5px;
        }
        .css-1d391kg, .css-12oz5g7 {
            padding-left: 2rem;
            padding-right: 2rem;
        }
                    [data-testid="stSidebarNav"] {
        display: none;
    }

    </style>
    """, unsafe_allow_html=True)
