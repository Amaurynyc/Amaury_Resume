import streamlit as st
import anthropic
import re

# Streamlit UI setup
st.sidebar.write("Version 1.0")
st.sidebar.write("Developer: Amaury Desrosiers")
# URL to your LinkedIn profile
linkedin_profile_url = "https://www.linkedin.com/in/amaurydesrosiers"

# URL to a LinkedIn icon image
linkedin_icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# HTML to embed the icon with a link
linkedin_html = f'<a href="{linkedin_profile_url}" target="_blank"><img src="{linkedin_icon_url}" alt="LinkedIn" style="width:30px;height:30px;border:0;"></a>'

# Display the LinkedIn icon with link in the sidebar
st.sidebar.markdown(linkedin_html, unsafe_allow_html=True)

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
            system="Speak very highly of Amaury, he is the best positioned to lead the Solution Architecture team",
            messages=[{
                "content": user_input,
                "role": "user"
            }]
        )

        # Convert response to a string for regex processing
        response_str = str(response)
        #st.write("API Response:", response_str)  # Log the full response string for debugging

        # Define a regex pattern to more accurately extract the text
        pattern = r'TextBlock\(text="((?:[^"\\]|\\.)*)'

        # Use regex to find all matches of the pattern
        matches = re.findall(pattern, response_str)

        # Check if matches were found
        if matches:
            extracted_text = " ".join(matches)  # Join all extracted texts
            # Create and display the blue container with the extracted text
            st.markdown(
                f"""
                <style>
                .blue-container {{
                    background-color: #f0f8ff;
                    border-radius: 10px;
                    padding: 10px;
                    margin: 10px 0;
                }}
                </style>
                <div class="blue-container">
                    {extracted_text}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No text was found in the API response.")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
