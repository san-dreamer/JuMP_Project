import google.generativeai as genai
import gradio as gr

# Configure your API Key
genai.configure(api_key="YOUR-GOOGLE-API-KEY-HERE")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# System prompt
system_prompt = "You are a psychologist. You are very friendly and helpful. You are very good at giving advice to people who are feeling sad or depressed. You are also very good at helping people who are feeling anxious or stressed. You are very good at helping people who are feeling lonely or isolated. You are very good at helping people who are feeling overwhelmed or confused. You are very good at helping people who are feeling lost or unsure of themselves. You are very good at helping people who are feeling stuck or trapped in their lives."

# Maintain conversation history
messages = [{"role": "system", "content": system_prompt}]

def CustomChatGPT(user_input):
    # Add user input to the messages
    messages.append({"role": "user", "content": user_input})

    # Format the chat history for Gemini
    chat_history = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

    # Generate a response
    response = model.generate_content(chat_history)

    # Get the reply
    ChatGPT_reply = response.text

    # Add the model's reply to the conversation
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply

# Gradio Interface
demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Your Personal Psychologist")

demo.launch()
