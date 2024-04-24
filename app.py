import streamlit as st
import anthropic

# Streamlit UI setup
st.sidebar.write("Version 1.0")
st.sidebar.write("Developer: Amaury")

# Initialize the client
client = anthropic.Anthropic(api_key=st.secrets["my_anthropic_api_key"])

# Chat interface
if user_input := st.text_input("How can I help with Wardley Mapping?"):
    try:
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
        
        # Extracting message content from the response
        if 'content' in response and isinstance(response['content'], list):
            # Iterate through each content block in the list
            for text_block in response['content']:
                if 'text' in text_block and text_block['type'] == 'text':
                    st.write(text_block['text'])
        else:
            st.error("The response from the API did not contain the expected 'content' data.")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
