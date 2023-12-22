# PoC-for-LLM-based-ChatBot-regarding-EU-AI-Regulation
** Proof of Concept (PoC) for Language Model-Based Chatbot regarding the EU AI Regulation**.

# Objective
Chatbots, empowered by artificial intelligence (AI), are computer programs designed to mimic human conversation. These sophisticated tools can be seamlessly integrated into websites, messaging applications, and various digital interfaces, offering benefits like cost reduction, enhanced efficiency, and heightened customer satisfaction.

ChatGPT possesses the unique capability to address queries involving data not encountered during its training, accommodating information that is either private or was unavailable prior to its 2021 knowledge cutoff.

This Proof of Concept (PoC) aims to leverage Large Language Model (LLM) technologies within chatbots to evaluate their potential advantages: cost-effectiveness, round-the-clock availability, minimized customer waiting times, tailored corporate information, and insightful analysis of customer behavior.

# Methodology
The data we have used related to the EU AI Laws and related regulations form different sources. We have used different pdf files describing the current AI Law.

As those PDF files are too large to send to the OpenAI models in a prompt, a solution must be used as current language models cannot consider large files with hundreds of pages. In the near future, as the size of input contexts increases, there will likely be situations for which the use of information retrieval techniques will not be technically necessary.

We use for this an information retrieval process throughout a data service. Our PDF files data are previously prepared with embeddings and stored in a FAISS vectorial database. Then, they are made available to restore from the database. In this process, the most suitable answer to the customer query to the database is recovered.

We use generative AI models, in particular several ChatGPT or GPT-4 related models:

* **"gpt-3.5-turbo"**: we use it to extract keywords from the user’s question by checking whether the question from the user does not respect GPT’s policy (e.g., malicious or sensitive,  input). 
* **"text-embedding-ada-002"**: we use it to create embeddings  which are a numerical representation of text that can be used to measure the relatedness between two pieces of text. We will save them into the FAISS vectorial database, and later we will recover them to answer the user's question. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about OpenAI latest embedding models in the “announcement blog post”. The “text-embedding-ada-002” is a designed to replace the previous 16 first-generation embedding models at a fraction of the cost. The reason to use it, it is better, cheaper, and simpler to use.
* **"text-davinci-003"**: we use it to answer the questions based on the text found by the FAISS vector database.






