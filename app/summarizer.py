import os
from environs import Env

from langchain import PromptTemplate
from langchain.llms import OpenAI

env = Env()
env.read_env(".env") # read .env file, if it exists

api_key = os.getenv("OPENAI_API_KEY")

def summarize_jd(job_description):
    template = """
    You are a career services professional with over 10 years of experience in the {industry} primarily operating in the {location}. You are tasked with finding skills from a job description for the role of {role}. Here is the job description:

    {job_description}

    Please analyze this job description to identify the skills, and categorize them as follows:

    - Job Title: Assess the job title as it may contain key terms that should be mirrored in the resume.
    - Responsibilities: Focus on responsibilities and action verbs that align with the role.
    - Requirements: Look for requirements such as education, experience, and certifications.

    Advise on how these identified skills can be effectively highlighted in a resume to ensure it aligns well with the requirements of this role. Please avoid cliches and generic answers, focusing on unique and specific insights related to the provided job description. Feel free to ask me as many follow-up questions as you'd like to clear any doubts, once you're done satisfying my current request.
    """

    prompt = PromptTemplate(
        input_variables=["industry", "location", "role", "job_description"],
        template=template,
    )

    # Formats the prompt with the addition of the input variables
    final_prompt = prompt.format(industry="Software Engineering", location="United States", role="Golang Engineer", job_description=job_description)

    llm = OpenAI(openai_api_key=api_key)

    summary = llm(final_prompt)

    return summary
