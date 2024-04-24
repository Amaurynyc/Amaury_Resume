import streamlit as st
import anthropic
import ast  # Import the abstract syntax tree module

# Streamlit UI setup
st.sidebar.write("Version 1.0")
st.sidebar.write("Developer: Amaury")

# Initialize the client with the API key from Streamlit's secrets
client = anthropic.Anthropic(api_key=st.secrets["my_anthropic_api_key"])

# Chat interface
user_input = st.text_input("How can I help with Wardley Mapping?. In your API response, I just want the text response, i want to be able to extract it easily.")

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

        # Convert the response to a string and then evaluate it to a Python object
        response_str = str(response)
        response_list = ast.literal_eval(response_str)

        # Assuming response_list is now a properly formatted list of dictionaries
        if response_list and isinstance(response_list, list):
            texts = [block['text'] for block in response_list if 'text' in block]
            extracted_text = " ".join(texts)
            st.write("Extracted Text:", extracted_text)
        else:
            st.error("No 'content' field found in the response, or response not in expected format.")

    except Exception as e:
        st.error(f"An error occurred while processing the response: {str(e)}")
