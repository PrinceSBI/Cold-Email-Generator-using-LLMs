# import streamlit as st

# st.title("📧 Cold Mail Generator")
# url_input = st.text_input("Enter a URL:", value="https://www.google.com/about/careers/applications/jobs/results/117034903765164742-senior-software-engineer-android-partner")
# submit_button = st.button("Submit")

# if submit_button:
#     st.code("Hello Hiring Manager, I am from Ansys", language='markdown')


import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text, one_job=True):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://www.google.com/about/careers/applications/jobs/results/117034903765164742-senior-software-engineer-android-partner")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            # print(jobs)
            if one_job==True:
                skills = jobs[0].get('skills', [])
                links = portfolio.query_links(skills)
                try:
                    email = llm.write_mail(jobs[0], links)
                except:
                    email = llm.write_mail(jobs, links)
                st.code(email, language='markdown')
            else:
                for job in jobs:
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)
                    st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == '__main__':
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)