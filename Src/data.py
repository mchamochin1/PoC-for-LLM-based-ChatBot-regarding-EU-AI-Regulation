# Data service
#
# This service makes you data prepared and available. The embeddings will be generated with the
# OpenAI API and stored in a FAISS vector store.


#!pip install tiktoken
#!pip install faiss-cpu
# langchain                    0.0.350
# openai                       1.3.9
# faiss-cpu                    1.7.4

import os
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

PDF_LOADER_PATH = './../../Docs/'
EMBEDINGS_MODEL_NAME="text-embedding-ada-002"
VECTORIALDB_NAME="db.faiss"

class DataService():

    def __init__(self):
        self.path = PDF_LOADER_PATH
        self.embedings_model = EMBEDINGS_MODEL_NAME

        # If vectorial database does not exist, i.e. fisrt time, then create it
        if not os.path.exists(VECTORIALDB_NAME):
            self.load_data_from_pdfs()
            self.store_data_to_vectorialdb()
            self.save_vectorialdb()
        else:
            self.embeddings = OpenAIEmbeddings(model=self.embedings_model)
            self.load_vectorialdb()

    def load_data_from_pdfs(self):
         # Load multiple files
        loaders = [UnstructuredPDFLoader(os.path.join(self.path, fn)) for fn in os.listdir(self.path)]

        self.all_documents = []

        for loader in loaders:
            #print("Loading raw document..." + loader.file_path)
            raw_documents = loader.load()

            #print("Splitting text...")
            text_splitter = CharacterTextSplitter(
                separator="\n\n",
                chunk_size=800,
                chunk_overlap=100,
                length_function=len,   #### CUANTO VALE LEN?
            )
            documents = text_splitter.split_documents(raw_documents)
            self.all_documents.extend(documents)

    def store_data_to_vectorialdb(self):
        self.embeddings = OpenAIEmbeddings(model=self.embedings_model)
        # Now each pages are embedded using the model and included in the Database
        self.db = FAISS.from_documents(self.all_documents, self.embeddings)

    def save_vectorialdb(self, vectorialdb_name: str = VECTORIALDB_NAME):
        # Persist the vectors locally on disk
        self.db.save_local(vectorialdb_name)
    
    def load_vectorialdb(self, vectorialdb_name: str = VECTORIALDB_NAME):
        # Load from local storage
        self.db = FAISS.load_local(vectorialdb_name, self.embeddings)

    def vectorialdb(self):
        return self.db

    def search_vectorialdb(self):
        pass

    def drop_vectorialdb_data(self):
        pass

