import streamlit as st
from main import app  # Importing your LangGraph agent
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Research Agent", page_icon="🤖")

st.title("🤖 Autonomous Research Agent")
st.markdown("### Powered by Llama 3 & LangGraph")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("What do you want to research?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run the Agent
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown(
            "🔎 *Researching... (Checking Vector DB & Synthesizing)*")

        # Run the LangGraph app
        try:
            inputs = {"question": prompt}
            result = app.invoke(inputs)

            # Extract final answer
            final_answer = result["generation"]

            # Show answer
            message_placeholder.markdown(final_answer)

            # Add assistant response to history
            st.session_state.messages.append(
                {"role": "assistant", "content": final_answer})

        except Exception as e:
            message_placeholder.error(f"Error: {e}")
