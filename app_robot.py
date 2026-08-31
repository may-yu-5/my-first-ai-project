import gradio as gr
from openai import OpenAI

client = OpenAI(
    api_key="sk-3fd940c1280948f2985491336cbe6f4e",
    base_url="https://api.deepseek.com"
)

messages = [{"role": "system", "content": "你是一个乐于助人的AI助手"}]

def chat_response(message):
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gr.Interface(
    fn=chat_response,
    inputs=gr.Textbox(label="输入你的问题", placeholder="在这里打字..."),
    outputs=gr.Textbox(label="AI的回答"),
    title="我的AI聊天机器人",
    description="AI会记住之前的对话内容"
)

demo.launch()
