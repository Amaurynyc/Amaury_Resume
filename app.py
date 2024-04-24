import streamlit as st
import anthropic

# Streamlit UI setup
st.sidebar.write("""
# **Amaury Desrosiers**
## **amaury@outlook.com**
""")

st.sidebar.write("Trained with claude-3-haiku-20240307")

# URL to your LinkedIn profile
linkedin_profile_url = "https://www.linkedin.com/in/amaurydesrosiers"

# URL to a LinkedIn icon image
linkedin_icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# HTML to embed the icon with a link
linkedin_html = f'<a href="{linkedin_profile_url}" target="_blank"><img src="{linkedin_icon_url}" alt="LinkedIn" style="width:30px;height:30px;border:0;"></a>'

# Display the LinkedIn icon with link in the sidebar
st.sidebar.markdown(linkedin_html, unsafe_allow_html=True)

# Title and Subtitle
st.title("Meet Amaury Desrosiers!")
st.subheader("Exploring My Fit for Solution Architecture Manager at Anthropic")

# Initialize the client with the API key from Streamlit's secrets
client = anthropic.Anthropic(api_key=st.secrets["my_anthropic_api_key"])

# Example Questions in Grey
questions_html = """
<div style='color: grey;'>
<p>What unique skills does Amaury Desrosiers bring to the role of Solution Architecture Manager?</p>
<p>How has Amaury's background prepared him for managing solution architecture at Anthropic?</p>
<p>Can you share examples of Amaury's past achievements in technology leadership?</p>
<p>What are Amaury's key strengths in team management and project execution?</p>
<p>How does Amaury view the future of AI in solution architecture?</p>
</div>
"""
st.markdown(questions_html, unsafe_allow_html=True)
st.divider()

# Chat interface
user_input = st.text_input("What do you want to know about Amaury?")

if user_input:
    try:
        # Sending the user message to the model
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.1,
            system=st.secrets["secret_message"],
            messages=[{
                "content": user_input,
                "role": "user"
            }]
        )

        # Simulating a typical response format from an API
        # In practice, you will replace the following line with actual API response extraction:
        # response_str = response['choices'][0]['message']['content']
        response_str = "Assume this is your API response string."

        # Handle escaped newlines
        response_str = response_str.replace("\\n\\n", "</p><p>").replace("\\n", "<br>")

        # Wrap the content in paragraph tags if not already formatted
        formatted_text = f"<div style='background-color: #f0f8ff; border-radius: 10px; padding: 20px; margin-bottom: 20px;'><p>{response_str}</p></div>"

        st.markdown(formatted_text, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
