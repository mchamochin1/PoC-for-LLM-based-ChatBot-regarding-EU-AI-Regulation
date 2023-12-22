# PoC-for-LLM-based-ChatBot-regarding-EU-AI-Regulation
**Proof of Concept (PoC) for Language Model-Based Chatbot regarding the EU AI Regulation**.

# Objective
Chatbots, empowered by artificial intelligence (AI), are computer programs designed to mimic human conversation. These sophisticated tools can be seamlessly integrated into websites, messaging applications, and various digital interfaces, offering benefits like cost reduction, enhanced efficiency, and heightened customer satisfaction.

ChatGPT possesses the unique capability to address queries involving data not encountered during its training, accommodating information that is either private or was unavailable prior to its 2021 knowledge cutoff.

**This Proof of Concept (PoC) aims to leverage Large Language Model (LLM) technologies within chatbots to evaluate their potential advantages: cost-effectiveness, round-the-clock availability, minimized customer waiting times, tailored corporate information, and insightful analysis of customer behavior.**

# Methodology
The data we have used related to the EU AI Laws and related regulations form different sources. We have used different pdf files describing the current AI Law.

As those PDF files are too large to send to the OpenAI models in a prompt, a solution must be used as current language models cannot consider large files with hundreds of pages. In the near future, as the size of input contexts increases, there will likely be situations for which the use of information retrieval techniques will not be technically necessary.

We use for this an information retrieval process throughout a data service. Our PDF files data are previously prepared with embeddings and stored in a **FAISS vectorial database**. Then, they are made available to restore from the database. In this process, the most suitable answer to the customer query to the database is recovered.

We use **generative AI model**s, in particular several ChatGPT or GPT-4 related models:
* **"gpt-3.5-turbo"**: we use it to extract keywords from the user’s question by checking whether the question from the user does not respect GPT’s policy (e.g., malicious or sensitive,  input). 
* **"text-embedding-ada-002"**: we use it to create embeddings  which are a numerical representation of text that can be used to measure the relatedness between two pieces of text. We will save them into the **FAISS vectorial database**, and later we will recover them to answer the user's question. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about OpenAI latest embedding models in the “announcement blog post”. The “text-embedding-ada-002” is a designed to replace the previous 16 first-generation embedding models at a fraction of the cost. The reason to use it, it is better, cheaper, and simpler to use.
* **"text-davinci-003"**: we use it to answer the questions based on the text found by the FAISS vector database.

We use the **LangChain framework** which is dedicated to developing LLM-powered apps. **LangChain** is a better fit to create bespoke language model-based applications that cater to chatbots or virtual assistants. LangChain is an open-source Python framework that facilitates the development of applications powered by large language models (LLMs) such as OpenAI’s GPT-3, Google’s BERT, and Meta’s LLaMA. LangChain offers a suite of tools, components, and interfaces that simplify the construction of LLM-centric applications. With LangChain, it becomes effortless to manage interactions with language models, seamlessly link different components, and incorporate resources such as APIs and databases. 

**LangChain’s key functionalities** are divided into modules: models, prompts, indexes, chains, agents, and memory. OpenAI and many other LLM providers are in this list of integrations. Most of these integrations need their API key to make a connection. For the OpenAI models, we do this setup with the key set in an **OPENAI_API_KEY** environment variable which should be defined in the .env file.

# Implementation
Here we focus on a more software oriented than “fine-tunning”. The idea is to use ChatGPT or GPT-4 models for information restitution, but not information retrieval: we do not expect the AI model to know the answer to the question. Rather, we ask it to formulate a well-thought answer based on text extracts we think could match the question. The idea is represented in this figure:

We use the following three components:
* An **"intent service"**: When the user submits a question to your application, the intent service’s role is to detect the intent of the question. Is the question relevant to your data? Perhaps you have multiple data sources: the intent service should detect which is the correct one to use. It could detect whether the question is related to your dataset (and if not, return a generic decline message), or add mechanisms to detect malicious intent. This service could also detect whether the question from the user does not respect our corporate’s policy, or perhaps contains sensitive information. We can save this questions in a database for a further analysis. For this PoC, however, our intent service is very simple— it extracts keywords from the user’s question using the ChatGPT "gpt-3.5-turbo" model. Thus, this intent service will be based on an OpenAI model in this example. 
* An **"data service"**: This service will take the output from the intent service and retrieve the correct information. This means our data will have already been prepared with embeddings and stored in the vectorial database, and then made it available to restore from the database with this service. Thus, we compare the embeddings between our data and the user’s query. The embeddings is generated with the “text-embedding-ada-002” model from OpenAI, and they are stored then in a vector database. The data service is easy to do with LangChain and embeddings.
* A **"response service"**: This service will take the output of the data service and generate from it an answer to the user’s question. We again use the "text-davinci-003" OpenAI model to generate the answer.

# Screen shots
We provide three examples to the questions provided:

**Question**: May you summarize the EU AI Act?

**Answer**: The EU AI Act is a landmark piece of legislation that seeks to create a comprehensive legal framework for the regulation of AI systems across the EU. It is intended to ensure the safety of AI systems on the EU market and provide legal certainty for investments and innovation in AI, while minimizing associated risks to consumers as well as compliance cost for providers. The EU AI Act prominently features a risk-based approach, defining four different risk classes, each of which covering different use cases of AI systems. It also includes provisions to support AI innovation in the EU and promote an ethical, safe, and trustworthy approach to AI.

<p align="center">
<img src="./Img/May you summarize the EU AI Act.png" alt="drawing" align="center" width="900"/>
</p>

**Question**: Why do we need to regulate the use of Artificial Intelligence?

**Answer**: The EU's AI Act is the first ever law on artificial intelligence, a regulatory framework that aims to make sure AI systems are safe, and that they respect the law and the EU's fundamental rights and values. It addresses risks to health, safety and fundamental rights, and also protects democracy, rule of law and the environment.

<p align="center">
<img src="./Img/Why do we need to regulate the use of AI.png" alt="drawing" align="center" width="900"/>
</p>

**Question**: What are the AI risk categories in EU law?

**Answer**: The EU AI Act categorises AI systems into four different risk classes, from Unacceptable (which are banned entirely) to High Risk (which are subject to specific obligations on the providers and deployers). The EU wants to ensure the safety of AI systems on the EU market and promote an ethical, safe, and trustworthy approach to AI.

<p align="center">
<img src="./Img/What are the AI risk categories in EU law.png" alt="drawing" align="center" width="900"/>
</p>











