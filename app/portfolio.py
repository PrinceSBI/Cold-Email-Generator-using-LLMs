import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="./app/resource/my_portfolio.csv"):
        self.file_path = file_path
        # print("################################################")
        # import os
        # current_directory = os.getcwd()
        # print(f"Current working directory: {current_directory}")
        # print(self.file_path)
        self.data = pd.read_csv(file_path)
        # Initializing the ChromaDB vector database
        self.chroma_client = chromadb.PersistentClient(path='./vectorestore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    # This code is used to store the contents in data frame to vector database
    def load_portfolio(self):
        if not self.collection.count():
            for _,row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"]+row["Discription"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        # return self.collection.query(query_texts=skills, n_results=3).get('metadatas', [])  # Looked at database and get results based on the distances
        return self.collection.query(query_texts=skills, n_results=3).get('documents', [])  # Looked at database and get results based on the distances