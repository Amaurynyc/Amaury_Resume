import streamlit as st
import os
from writerai import Writer
import re

# Streamlit UI setup
st.sidebar.write("""
# **Amaury Desrosiers**
## **amaury@outlook.com**
""")

st.sidebar.write("WRITER palmyra-x-002-instruct")

st.sidebar.markdown("""
[Solution Architect](https://jobs.ashbyhq.com/writer/f185ea96-e519-47fa-aeeb-97682e8968e5)
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
st.title("Meet Amaury Desrosiers!")
st.markdown("**Exploring Amaury's fit for Solution Architect at Writer**")



# Example Questions in Grey
questions_html = """
<div style='color: grey;'>
<p>What unique skills does Amaury Desrosiers bring to the role of Solution Architect?</p>
<p>How has Amaury's background prepared him for to be a solution architects at Writer?</p>
<p>Can you share examples of Amaury's past achievements in technology leadership?</p>
</div>
"""
st.markdown(questions_html, unsafe_allow_html=True)
st.divider()



# Chat interface
user_input = st.text_input(" ℹ️ What do you want to know about Amaury?", value="What specific experiences would set him for success in this role?")

context=st.secrets["secret_message"]


if user_input:
    try:
        # Sending the user message to the model
        
        client = Writer(
        # This is the default and can be omitted
        api_key="euHnjBi7d7qSg9pFGxKbj5FoBrDLlcwr",
        )
        completion = client.completions.create(
        model="palmyra-x-002-instruct",
        best_of=1,
        prompt=f"{context}.{user_input}. The answer should only have a couple of paragraph. Pick the best answer",
        )
        response = completion.choices[0].text       

        # Print the full API response
        st.write(completion.choices[0].text)


        st.markdown(
            f"""
            <style>
            .blue-container {{
                background-color: #8eb2fa;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
            }}
            </style>
            {completion.choices[0].text}
            """,
            unsafe_allow_html=True
        )


    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
