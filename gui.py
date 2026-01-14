import streamlit as st
from main import app  
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Research Agent", page_icon="🤖")

st.title("🤖 Autonomous Research Agent")
st.markdown("### Powered by Llama 3 & LangGraph")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What do you want to research?"):
    y
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(
            "🔎 *Researching... (Checking Vector DB & Synthesizing)*")

      
        try:
            inputs = {"question": prompt}
            result = app.invoke(inputs)

          
            final_answer = result["generation"]

            
            message_placeholder.markdown(final_answer)

           
            st.session_state.messages.append(
                {"role": "assistant", "content": final_answer})

        except Exception as e:
            message_placeholder.error(f"Error: {e}")

