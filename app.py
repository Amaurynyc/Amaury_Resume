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

        # Log the response to inspect the structure, temporarily for debugging
        st.write("API Response:", response)

        st.write("Text Extract:", response["content"][0]["text"])

    

        # Extracting and displaying text from messages
        if 'messages' in response:
            for message in response['messages']:
                # Check if 'content' is present and is a list
                if 'content' in message and isinstance(message['content'], list):
                    # Extract text from each TextBlock if present
                    texts = [block['text'] for block in message['content'] if 'text' in block]
                    # Display each piece of text
                    for text in texts:
                        st.write(text)
                else:
                    st.write("No text content available in this message.")
        else:
            st.error("The response from the API did not contain the expected 'messages' data.")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
