from setup import load_dotenv
from document_loader import clone_repo_and_load_documents, setup_embeddings_and_db
from chat_model import setup_chat_model_and_retrieval_chain

def main():
    # Load environment and setup
    load_dotenv()
    
    # Clone repo and load documents
    documents = clone_repo_and_load_documents()
    
    # Setup embeddings and database
    db = setup_embeddings_and_db(documents)
    
    # Setup chat model and retrieval chain
    qa = setup_chat_model_and_retrieval_chain(db)
    
    # Example question and chat history
    chat_history = []
    question = "How can I load a source code as documents, for a QA over code, splitting the code in classes and functions?"
    
    # Get result and update chat history
    result = qa({"question": question, "chat_history": chat_history})
    chat_history.append((question, result["answer"]))
    
    # Print result
    print(result["answer"])

if __name__ == "__main__":
    main()
