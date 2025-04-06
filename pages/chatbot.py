import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.chatbot_service import get_suggested_questions, generate_response

def chatbot_page():
    st.title("AI Agricultural Assistant")
    show_extra_menu()
    
    # Initialize chat history if not already done
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I'm your agricultural assistant. How can I help you today?"}
        ]
    
    # Suggested questions sidebar
    st.sidebar.header("Suggested Questions")
    suggested_questions = get_suggested_questions()
    
    for question in suggested_questions:
        if st.sidebar.button(question):
            st.session_state.chat_messages.append({"role": "user", "content": question})
            
            # Generate response based on the question
            response = generate_response(question)
            
            # Add assistant response
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    # User input
    user_input = st.chat_input("Ask about crops, diseases, weather, or farming techniques...")
    
    if user_input:
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        
        # Generate response
        response_text = generate_response(user_input)
        
        # Add assistant response
        st.session_state.chat_messages.append({"role": "assistant", "content": response_text})
        st.rerun()
    
    back_to_dashboard()
