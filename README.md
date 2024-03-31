# LangChain Code QA System

This project demonstrates how to use the LangChain library to perform a Question-Answering (QA) system over source code, specifically focusing on the LangChain repository. The system is designed to load source code as documents, split the code into classes and functions, and then use a conversational retrieval chain to answer questions about the code.

## Dependencies

The project requires the following Python packages:

- langchain[llms]>=0.0.218
- chromadb
- sentence_transformers
- tiktoken
- GitPython
- python-dotenv

These dependencies are listed in the `requirements.txt` file.

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:


4. Ensure you have a `.env` file in the project root with the necessary environment variables.

## Running the Code

To run the code, execute the main script:

```bash 
pip install -r requirements.txt
```

4. Ensure you have a `.env` file in the project root with the necessary environment variables.

## Running the Code

To run the code, execute the main script:

```bash 
python main.py
```

This script will clone the LangChain repository, load the source code as documents, set up the embeddings and database, and then use a conversational retrieval chain to answer questions about the code.

## Example Question

The example question provided in the code is:

What is the class hierarchy? 

```bash 
**Answer**: The class hierarchy in object-oriented programming is the structure that forms when classes are derived from other classes. The derived class is a subclass of the base class also known as the superclass. This hierarchy is formed based on the concept of inheritance in object-oriented programming where a subclass inherits the properties and functionalities of the superclass. 

In the given context, we have the following examples of class hierarchies:

1. `BaseCallbackHandler --> <name>CallbackHandler` means `BaseCallbackHandler` is a base class and `<name>CallbackHandler` (like `AimCallbackHandler`, `ArgillaCallbackHandler` etc.) are derived classes that inherit from `BaseCallbackHandler`.

2. `BaseLoader --> <name>Loader` means `BaseLoader` is a base class and `<name>Loader` (like `TextLoader`, `UnstructuredFileLoader` etc.) are derived classes that inherit from `BaseLoader`.

3. `ToolMetaclass --> BaseTool --> <name>Tool` means `ToolMetaclass` is a base class, `BaseTool` is a derived class that inherits from `ToolMetaclass`, and `<name>Tool` (like `AIPluginTool`, `BaseGraphQLTool` etc.) are further derived classes that inherit from `BaseTool`. 

-> **Question**: What classes are derived from the Chain class? 

**Answer**: The classes that are derived from the Chain class are:

1. LLMSummarizationCheckerChain
2. MapReduceChain
3. OpenAIModerationChain
4. NatBotChain
5. QAGenerationChain
6. QAWithSourcesChain
7. RetrievalQAWithSourcesChain
8. VectorDBQAWithSourcesChain
9. RetrievalQA
10. VectorDBQA
11. LLMRouterChain
12. MultiPromptChain
13. MultiRetrievalQAChain
14. MultiRouteChain
15. RouterChain
16. SequentialChain
17. SimpleSequentialChain
18. TransformChain
19. BaseConversationalRetrievalChain
20. ConstitutionalChain 
```
The system attempt to answer this question based on the source code in the LangChain repository.

