import os
import streamlit as st
import anthropic
import re

st.title("Job Referral Generator")

# Get the Anthropic API key from an environment variable
api_key = os.environ.get("ANTHROPIC_API_KEY")

# Initialize the Anthropic client
client = anthropic.Client(api_key)

user_input = st.text_area("Enter your profile and the job description:")

if st.button("Generate Referral"):
    if user_input.strip() == "":
        st.warning("Please provide your profile and the job description.")
    else:
        try:
            # Call the Anthropic API to generate the referral
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

            # Convert response to a string for regex processing
            response_str = str(response)

            # Define a regex pattern to more accurately extract the text
            pattern = r'TextBlock\\(text="((?:\[^"\\\\\]|\\\\.)\*)'

            # Use regex to find all matches of the pattern
            matches = re.findall(pattern, response_str)

            # Check if matches were found
            if matches:
                extracted_text = " ".join(matches) # Join all extracted texts

                # Split the referral into paragraphs based on "\n\n"
                paragraphs = extracted_text.split("\\n\\n")

                # Initialize an empty string to store the formatted referral
                formatted_referral = ""

                # Iterate over each paragraph
                for paragraph in paragraphs:
                    # Check if the paragraph starts with "- " indicating a bullet point
                    if paragraph.startswith("- "):
                        # Add the bullet point to the formatted referral
                        formatted_referral += "- " + paragraph[2:] + "\n\n"
                    else:
                        # Add the paragraph to the formatted referral
                        formatted_referral += paragraph + "\n\n"

                # Create and display the blue container with the formatted referral
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
                    {formatted_referral}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error("No text was found in the API response.")

        except Exception as e:
            st.error(f"An error occurred while fetching the response: {str(e)}")
