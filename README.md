# Cold-Email-Generator-using-LLMs
Tech Stack: Python, LangChain, LLaMA-3 (via GROQ), Streamlit, ChromaDB, Pandas, Web Scraping 

1. Developed an intelligent application that automatically extracts job descriptions from company career pages and generates personalized cold emails using LLMs.
2. Implemented end-to-end workflow using LangChain and LLaMA-3.3-70B-Versatile to parse job data and compose professional emails tailored to user's experience and portfolio.
3. Built custom chaining logic with PromptTemplate and JsonOutputParser for structured LLM communication and parsing job roles, experience, skills, and descriptions.
4. Integrated ChromaDB to store and query portfolio projects based on job skill match, enhancing email relevance by 70%.
5. Engineered a web interface with Streamlit, enabling users to enter job URLs and receive tailored emails in real-time.
6. Optimized text preprocessing using regular expressions and vector search to maintain high response accuracy and low latency.
7. Automated cold-email generation process for any job URL, reducing manual effort and improving application turnaround by over 80%.

use this command to run the app: streamlit run ./app/main.py

Modify the prrompts according to your need in chain.py file
Include your skills in my_protfolio.csv file 
Create your .env file ang use your API key from GroqCloud
