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
            prompt=f"You need to speak about Amaury as a very talented and good person\nUser: {user_input}\nAssistant:",
        )

        # Extract and display the response text
        extracted_text = response.completion

        # Split the response into bullet points
        bullet_points = extracted_text.split("\\n\\n")

        # Format the bullet points using Markdown syntax
        formatted_text = "\n".join([f"- {point.strip()}" for point in bullet_points if point.strip()])

        # Display the formatted bullet points using st.markdown()
        st.markdown(formatted_text)

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
