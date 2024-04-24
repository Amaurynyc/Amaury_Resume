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
            system="Amaury_Background = "Here is Amaury  resume for context : Dynamic Solution Consulting leader with 15+ years of experience in the technology industry.
Proven track record of success in starting, leading Solution Consulting teams, and delivering results.
Expertise in multiple industries : A.I., Machine Learning, Online Fraud Prevention, Pricing, Banking.

EXPERIENCE

VP of Solution Consulting 					 	New York City  Feb 2022 - Current
PRICEMOOV Global provider of next-generation price management and optimization solutions      
MISSION
Start the solution consulting practice and strategically evolve the sales methodology to a scalable SAAS framework.
Define the vision and align growth objectives with the Executive Leadership team.
Implement scalable processes to increase sales, accelerate engagement model and customer usage.
Identify bottlenecks in the sales process and implement effective strategies that reduced deal durations and increased win rates.
ACTIONS
Hire, coach and lead the global solution consulting.
Implemented best practices and processes: Discovery questions standards, demo environments and scripts, technical qualification, collateral for each stage of the sales process.
Formalized the engagement model with clearly defined steps and collateral.
Leverage data to standardize use cases, pain points, benefits, and value proposition for each product (Command of Message (CoM), MEDDICC).
Established a robust partnership with the Product Team, instituting a cohesive process that directly influenced and advanced the product roadmap to match the GTM strategy.
IMPACTS
Reduce the average deal duration by 30% and increase Sales growth by 60%.
Increase the win rate of qualified deals by 45% and put in place scalable processes.


Director of Solution Consulting 		 			New York City  Nov 2019 - Feb 2022
FORTER Global leader in e-commerce fraud prevention solutions leveraging A.I. 
MISSION  
Start the Solution Consulting practice to support the global growth, increase efficiency and revenue.
Coach, mentor and set the vision for the team.
Influence roadmap and C-Level strategy based on the team feedback.
Empower the sales team with expertise to simply explain our A.I. models and their value to C-Level audiences. 
ACTIONS
Instituted a structured feedback mechanism with Product, ensuring roadmap alignment with our GTM strategy.
Standardized the sales engagement model with scripts, value based workshop, technical deep dive, ROI calculation, standard collaterals, etc.
Cultivated strategic partnerships with leaders of Data Science, Engineering, Product, and GTM to foster collaboration.
Defined comprehensive onboarding procedures, certification program, competitive battlecards, and enablement program to onboard better and faster new team members.
Set in place operational KPIs to track performance, team efficiency as well as RACI model.
IMPACTS
Hired and managed 15+ team members across US, EU and APAC.
Increased by 20% the sales of emerging products beyond our core offering.
Improved the average win rates of opportunities across all regions (x 2.5).
Improved the average deal size of a deal by 75%.
Reduced by 50% the onboarding time of newly hired Solution Consultants.

Director of Presales (promoted from Senior Presales Consultant)	 	New York City  Jul 2016 - Nov 2019
AYASDI Leader in AI-driven data analytics, revolutionizing industries with advanced ML insights	           
MISSION
First Presales hire, tasked to build the Solution Consulting activity. 
Transition the sales approach to a value selling framework, pivoting from a feature-centric to a value-centric model.
Operationalize the POC engagements with our data science team to scale the business and increase revenue.
ACTIONS
Launched the development of collateral material to showcase the value of our A.I. platform to C-Level audience.
Established POC benchmarks with the Data Science teams to ensure clarity in success criteria and execution.
Initiated enablement program (RFP engine, demo env., scripts, templates,) to enable scale.
Defined qualification and sales engagement model to structure the engagement model.
Empower the sales team with clear ROI calculators to demonstrate the value of the platform.
Led and executed comprehensive scoping, tailored presentations, and POCs for major global banks.
IMPACTS
Hired and led a global team of 5 Presales, instituted regular coaching sessions to develop team members.
Improved by 30% the team win rate, and increased the average deal size by +30%.
Increased new revenue by 40% with new demo framework and value selling approach.


Senior Presales Consultant 						New York City Sep 2015 - Jul 2016
QUANTIFI Top tiers provider of risk, analytics, and trading solutions
	      
First Presales hire, tasked to build the Solution Consulting activity.
Conducted targeted platform demonstrations for key players within the hedge funds and asset manager markets.
Assessed client operational frameworks, articulating the unique value of our solutions for their infrastructure.
Led the Presales initiatives on a variety of targets (hedge funds and asset managers). 
Worked closely with the Sales team to design the Go-To-Market strategy for credit hedge funds. 


Senior Presales Consultant (promoted from Sr Project Mgr and Consultant)	New York City Sep 2006 - Sep 2015
MISYS - SOPHIS Now Finastra, one of the world s largest banking software companies
 	 	          
Ran Presales workshops and demos to large prospects contributing to the acquisition of new clients.
Steered the implementation of projects for large banks, coordinating and guiding teams of 10+ consultants and dev.
Fostered and maintained strong relationships with key clients, leveraging feedback to shape product roadmaps.
Delivered specialized consulting to maximize our platform s potential tailored to their specific needs.


EDUCATION

UCL			      MSc Telecommunications 			   	  London	2005-2006
CENTRALESUPELEC	      MSc Computer Science and Electrical Engineering	  Paris		2003-2006",
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
