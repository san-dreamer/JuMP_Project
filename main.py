from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

template = """
Answer the questions below.
Here is the conversation history: {context}
Question: {question}
Answer:
"""

model =  OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome, I am your AI Psychologist!")
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": question})
        print("\nAnswer:", result)
        context += f"User: {question}\nAssistant: {result}\n"

if __name__ == "__main__":
    handle_conversation()   

result = chain.invoke({"context": "", "question": "hey, how are you?"})
print(result)