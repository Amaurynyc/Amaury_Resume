import streamlit as st
import anthropic
import re

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

        # Convert response to a string for regex processing
        response_str = str(response)
        st.write("API Response:", response_str)  # Log the full response string for debugging

        # Define a regex pattern to more accurately extract the text
        pattern = r'TextBlock\(text="((?:[^"\\]|\\.)*)'

        # Use regex to find all matches of the pattern
        matches = re.findall(pattern, response_str)

        # Check if matches were found
        if matches:
            extracted_text = " ".join(matches)  # Join all extracted texts
            # Display each extracted text in a blue chat message box
            for text in matches:
                st.chat_message(text, is_user=False)  # is_user=False for bot responses, True for user messages
        else:
            st.error("No text was found in the API response.")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")

# Optionally, display the user's input in the chat as well for full context
if user_input:
    st.chat_message(user_input, is_user=True)  # Display user input in the chat for context
