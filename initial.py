import os
# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.chains import create_history_aware_retriever, create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv
# load_dotenv()

# cwd=os.getcwd()
# db=os.path.join(cwd,'db')
# embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

# vector_db=Chroma(persist_directory=db,embedding_function=embeddings)

# retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
# llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# contextualize_q_system_prompt = (
#     "Given a chat history and the latest user question "
#     "which might reference context in the chat history, "
#     "formulate a standalone question which can be understood "
#     "without the chat history. Do NOT answer the question, just "
#     "return a suitable question that helps you to search anything related to the question in the vector DB"
# )

# contextualize_q_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", contextualize_q_system_prompt),
#         MessagesPlaceholder("chat_history"),
#         ("human", "{input}"),
#     ]
#     )

# history_aware_retriever = create_history_aware_retriever(
#     llm, retriever, contextualize_q_prompt
# )

# qa_system_prompt = (
#     "You are an assistant for helping people to know about our company. Use "
#     "the following pieces of retrieved context to answer the "
#     "question. "
#     "\n\n"
#     "{context}"
# )

# qa_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", qa_system_prompt),
#         MessagesPlaceholder("chat_history"),
#         ("human", "{input}"),
#     ]
# )

# question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

# rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
# def continual_chat():
#     print("Start chatting with the AI! Type 'exit' to end the conversation.")
#     chat_history = []  # Collect chat history here (a sequence of messages)
#     while True:
#         query = input("You: ")
#         if query.lower() == "exit":
#             break
#         # Process the user's query through the retrieval chain
#         result = rag_chain.invoke({"input": query, "chat_history": chat_history})
#         # Display the AI's response
#         print(f"IqBot: {result['answer']}")
#         # Update the chat history
#         chat_history.append(HumanMessage(content=query))
#         chat_history.append(AIMessage(content=result["answer"]))

# continual_chat()

#################
