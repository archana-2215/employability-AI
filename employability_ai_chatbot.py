import gradio as gr
from transformers import pipeline

# Load fast AI model
chatbot = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=120
)

SYSTEM_PROMPT = """
You are an AI assistant for Employability Awareness.
Help students with:
- career guidance
- resume improvement
- job interview preparation
- skills needed for jobs
- course recommendations
Give short and helpful answers.
"""

def respond(message, history):

    prompt = SYSTEM_PROMPT + "\nUser: " + message + "\nAssistant:"

    result = chatbot(prompt)

    reply = result[0]["generated_text"]

    return reply


demo = gr.ChatInterface(
    fn=respond,
    title="🤖 AI Employability Awareness Chatbot",
    description="Ask about careers, skills, resume tips, and interview preparation.",
    theme="soft"
)

demo.launch()