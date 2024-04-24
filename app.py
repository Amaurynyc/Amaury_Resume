import streamlit as st
import anthropic
import re
import os


# Streamlit UI setup
st.sidebar.write("""
# **Amaury Desrosiers**
## **amaury@outlook.com**
""")

st.sidebar.write("""
 
Trained with claude-3-haiku-20240307
""")

# URL to your LinkedIn profile
linkedin_profile_url = "https://www.linkedin.com/in/amaurydesrosiers"

# URL to a LinkedIn icon image
linkedin_icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# HTML to embed the icon with a link
linkedin_html = f'<a href="{linkedin_profile_url}" target="_blank"><img src="{linkedin_icon_url}" alt="LinkedIn" style="width:30px;height:30px;border:0;"></a>'

# Display the LinkedIn icon with link in the sidebar
st.sidebar.markdown(linkedin_html, unsafe_allow_html=True)

# Title and Subtitle
st.title("Meet Amaury Desrosiers !")
st.subheader("Exploring My Fit for Solution Architecture Manager at Anthropic")


# Initialize the client with the API key from Streamlit's secrets
client = anthropic.Anthropic(api_key=st.secrets["my_anthropic_api_key"])

# Example Questions in Grey

questions_html = """
<div style='color: grey;'>
<p style='margin-bottom: 5px;'>What unique skills does Amaury Desrosiers bring to the role of Solution Architecture Manager?</p>
<p style='margin-bottom: 5px;'>How has Amaury's background prepared him for managing solution architecture at Anthropic?</p>
<p style='margin-bottom: 5px;'>Can you share examples of Amaury's past achievements in technology leadership?</p>
<p style='margin-bottom: 5px;'>What are Amaury's key strengths in team management and project execution?</p>
<p style='margin-bottom: 5px;'>How does Amaury view the future of AI in solution architecture?</p>
</div>
"""

st.markdown(questions_html, unsafe_allow_html=True)
st.divider()
# Chat interface
user_input = st.text_input("What do you want to know about Amaury?")

if user_input:
    try:
        # Assume you have a function 'send_query_to_model' to send queries to your model
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.1,
            system=st.secrets["secret_message"],
            messages=[{"content": user_input, "role": "user"}]
        )
        
        # Convert response to a string for regex processing
        response_str = str(response)

        # Extracted text formatting
        matches = re.findall(pattern, response_str)
        if matches:
            extracted_text = " ".join(matches)  # Join all extracted texts
            formatted_text = format_text_for_markdown(extracted_text)  # Format text for Markdown display
            # Display formatted text in a custom styled container
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
                <div class="blue-container">{formatted_text}</div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("No text was found in the API response.")
            
    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")

    except Exception as e:
        st.error(f"An error occurred while fetching the response: {str(e)}")
