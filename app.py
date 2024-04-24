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

    if 'content' in response and isinstance(response['content'], list):
        # Extracting the text from each TextBlock in the content list
        formatted_output = "\n".join(text_block['text'] for text_block in response['content'] if 'text' in text_block)
        # Writing the formatted output to a text file
        with open('output.txt', 'w') as file:
            file.write(formatted_output)
        print("Output has been successfully saved to 'output.txt'.")
    else:
        print("Response content is not in the expected list format:", response)
except Exception as e:
    print("An error occurred:", str(e))
