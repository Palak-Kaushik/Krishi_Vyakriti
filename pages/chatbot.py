import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.chatbot_service import get_suggested_questions, generate_response

def chatbot_page():
    st.title("AI Agricultural Assistant")
    show_extra_menu()
    
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I'm your agricultural assistant. How can I help you today?"}
        ]
    
    st.sidebar.header("Suggested Questions")
    suggested_questions = get_suggested_questions()
    
    for question in suggested_questions:
        if st.sidebar.button(question):
            st.session_state.chat_messages.append({"role": "user", "content": question})
            
            response = generate_response(question)
            
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    user_input = st.chat_input("Ask about crops, diseases, weather, or farming techniques...")
    
    if user_input:
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        
        response_text = generate_response(user_input)
        
        st.session_state.chat_messages.append({"role": "assistant", "content": response_text})
        st.rerun()
    
    back_to_dashboard()

