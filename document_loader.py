from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from git import Repo
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

def clone_repo_and_load_documents():
    repo = Repo.clone_from(
        "https://github.com/hwchase17/langchain", to_path="/tmp/test_repo"
    )
    loader = GenericLoader.from_filesystem(
        "/tmp/test_repo/langchain",
        glob="**/*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500)
    )
    documents = loader.load()
    return documents

def setup_embeddings_and_db(documents):
    python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=2000, chunk_overlap=200)
    texts = python_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(disallowed_special=())
    db = Chroma.from_documents(texts, embeddings)
    return db
