from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

def setup_chat_model_and_retrieval_chain(db):
    retriever = db.as_retriever(
        search_type="mmr", # You can also experiment with "similarity"
        search_kwargs={"k": 8},
    )
    llm = ChatOpenAI(temperature=0)
    qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)
    return qa
