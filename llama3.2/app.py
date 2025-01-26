import streamlit as st
from transformers import pipeline
import torch
import os

@st.cache_resource
def load_model():
    # Retrieve the Hugging Face token from environment variables
    hf_token = os.getenv("HUGGINGFACE_TOKEN")
    if not hf_token:
        raise ValueError("Hugging Face token is not set. Please provide the token as an environment variable.")

    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        use_auth_token=hf_token,
    )
    return pipe

st.title("Chatbot")
st.subheader("Speak to a svastikkka AI, matey!")
st.write("Loading model... this might take a while.")
pipe = load_model()
st.write("Model loaded! Start chattin', landlubber!")
messages = [
    {"role": "system", "content": "You are a svastikkka chatbot who always responds in svastikkka speak!"}
]
user_input = st.text_input("What do ye want to say to the svastikkka AI?")
if st.button("Send"):
    if user_input.strip():
        messages.append({"role": "user", "content": user_input})
        with st.spinner("The svastikkka is thinkin'..."):
            try:
                outputs = pipe(messages, max_new_tokens=256)
                svastikkka_response = outputs[0]["generated_text"]
                messages.append({"role": "assistant", "content": svastikkka_response})
                st.write(f"**svastikkka AI:** {svastikkka_response}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Type somethin' fer the svastikkka!")
st.subheader("Chat History")
for msg in messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.write(f"**svastikkka AI:** {msg['content']}")

