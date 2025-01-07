from langchain_community.llms import ollama,Ollama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
# from langchain.schema.output_parser import StrOutputParser
from langchain.schema.output_parser import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
# llm = Ollama(base_url="http://localhost:11434",model="llama2")
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# model=ChatOpenAI(model="gpt-3.5-turbo")

chat_history=[]
messages=[("system","You are a personal assistant of {name}, resolve the queries and assist him"),MessagesPlaceholder("chat_history")]
prompt_template=ChatPromptTemplate.from_messages(messages)
# system_message = SystemMessage(content = " You are a helpful AI assistant. ")
# chat_history.append(system_message)
name = input("Enter Your Name: ")
while True:
    query =  input(f"{name}: ")
    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))
    # print(prompt_template.invoke({"name":name,}))

    # result = model.invoke(chat_history)
    chain = prompt_template|model|StrOutputParser()
    result = chain.invoke({"name":name,"chat_history":chat_history})
    response = result
    chat_history.append(AIMessage(content=response))

    print(f"AI {response}")
