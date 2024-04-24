import streamlit as st
import anthropic

# Streamlit UI setup
st.sidebar.write("Version 1.0")
st.sidebar.write("Developer: Amaury")

# Initialize the client with the API key from Streamlit's secrets
client = anthropic.Anthropic(api_key=st.secrets["my_anthropic_api_key"])

# Chat interface
user_input = st.text_input("How can I help with Wardley Mapping?")

if user_input:
    try:
        # Sending the user message to the model
        response = client.messages.create(
            model="claude-2.1",
            max_tokens=100,
            temperature=0.1,
            system="You need to speak about Amaury as a very talented and good person",
            messages=[{
                "content": user_input,
                "role": "user"
            }]
        )

        # Attempt to access the content if it is in the expected format
        if hasattr(response, 'content'):
            texts = [block.text for block in response.content if hasattr(block, 'text')]
            extracted_text = " ".join(texts)
            st.code("Extracted Text:", extracted_text)
        else:
            st.error("No 'content' field found in the response, or response not in expected format.")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
