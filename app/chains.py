import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()       # Used to get in the .env file to access the environment variable

os.getenv("GROQ_API_KEY")       # Used to access the environment variables in the .env file 


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),       # Used to access the environment variables in the .env file which is the API Key
            model_name='llama-3.3-70b-versatile'
        )
        self.imp_links = [
            {'LinkedIn': 'https://www.linkedin.com/in/shreyas-gs-311012154/'},
            {'Portfolio': 'https://princesbi.github.io/'},
            {'GitHub': 'https://github.com/PrinceSBI'}
        ]

    def extract_jobs(self, cleaned_text):
        # Create a prompt to LLM using PromptTemplate.from_template
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the 
            following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm   # Feed the Prompt to LLM using chain method
        res = chain_extract.invoke(input={'page_data': cleaned_text})  # Get the response of LLM using in .invoke
        # print(res.content)      # The output obtained is JSON in string format

        try:
            # This code is used to convert the string from the response to JSON format
            json_parcer = JsonOutputParser()
            res = json_parcer.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
        return res if isinstance(res, list) else [res]
    

    def write_mail(self, job, projects):
        # Create a prompt to LLM using PromptTemplate.from_template
        prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                
                ### INSTRUCTION: Write an email to Hearing Manager
                You are Shreyas GS, an R&D Verification Engineer at Ansys Software Pvt Ltd and have 2 years of overall professional experience. 

                At Ansys, 
                I worked on Working in APDL Verification Team, responsible for validating structural mechanics capabilities of the ANSYS solver. 
                Actively contributed to tracking & resolving 50+ bugs, coordinating with development teams to identify, reproduce, & close issues within sprint cycles.
                Created Python scripts to automate 500+ verification files, reducing manual workload by over 70% & increasing regression efficiency & consistency.
                Conducted GPU acceleration validation with 1000+ test cases, improving solver performance and stability.
                
                My Previous company was BlueHat Solutions Pvt Ltd were I worked as an Analysis Engineer.
                At BlueHat,
                Conducted EDA on 8 million+ FDR entries, extracting actionable insights on aircraft behavior & critical event.
                Developed Python script to extract and synchronize force data from CFD and FEM files by aligning grid coordinate
                systems with 98% mapping accuracy.
                Utilized ML & FFT for Flight Data Analysis, identified flight maneuver & natural frequency for Flight Data.
                Automated conversion of unstructured output into structured data using Python, reduced data processing time by 80%
                Automated weight & CG calculations for weapon integration using Python, enhancing efficiency by 40%.
                Developed Python tool to compute critical loads from all load combinations & improving design accuracy by 90%.

                Over the 2 years experience, we have worked on Data Analysis, Developing and Testing various FEA based solutions. 
                Your job is to write a cold email to the HR regarding the job mentioned above describing the How you are best fit for the role
                in fulfilling their needs.
                Some information regarding my relevant Projects: {project_list}
                Also add the following to showcase LinkedIn and Portfolio: {Imp_Lnks}
                Remember you are Shreyas GS, R&D Verification Engineer at Ansys Software Pvt Ltd immediate joiner with 2 years of experience. 
                Do not provide a preamble.
                ### EMAIL (NO PREAMBLE):
                
                """
                )

        chain_email = prompt_email | self.llm   # Feed the Prompt to LLM using chain method
        res = chain_email.invoke({"job_description": str(job), "Imp_Lnks": self.imp_links, "project_list": projects})  # Get the response of LLM using in .invoke
        # print(res.content)      # The output response obtained in string format

        return res.content
    

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))