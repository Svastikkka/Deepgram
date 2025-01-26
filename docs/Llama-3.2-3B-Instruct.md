# Overview
- A 3-billion-parameter language model developed by Meta
- Designed for instruction-based tasks
- Released on September 25, 2024

# Intended Use Cases:

- Assistant-like Chat and Agentic Applications: Tailored for conversational agents and tasks like knowledge retrieval and summarization.
- Mobile AI-powered Writing Assistants: Suitable for on-device applications with limited computational resources.
- Query and Prompt Rewriting: Enhances the clarity and effectiveness of user inputs.

# Installation

## Required dependencies
```bash
pip install torch --index-url https://pypi.org/simple/
pip install transformers accelerate huggingface_hub streamlit --index-url https://pypi.org/simple/
```

## Verify
```bash
python -c "import transformers; print(transformers.__version__)"
python -c "import accelerate; print(accelerate.__version__)"
python -c "import huggingface_hub; print(huggingface_hub.__version__)"
```

## Login to huggingface
```bash
huggingface-cli login
```
*Note*: Token will be required

# How to use

1. Create app.py file

```python
import streamlit as st
from transformers import pipeline
import torch

# Load the model
@st.cache_resource
def load_model():
    model_id = "meta-llama/Llama-3.2-3B-Instruct"
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    return pipe

st.title("Chatbot")
st.subheader("Speak to a AI")
st.write("Loading model this might take a while.")
pipe = load_model()
st.write("Model loaded! Start chatting', landlubber!")
messages = [
    {"role": "system", "content": "You are a chatbot who always responds in speak!"}
]
user_input = st.text_input("What do ye want to say to the AI?")

if st.button("Send"):
    if user_input.strip():
        messages.append({"role": "user", "content": user_input})
        with st.spinner("The chatbot is thinkin'..."):
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
```

2. Run the app
```bash
streamlit run app.py
```

3. Create a dockerfile
```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY app.py /app/app.py
RUN apt-get update && apt-get install -y
RUN pip install --no-cache-dir \
    streamlit \
    transformers \
    torch \
    accelerate
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

4. Build Image
```bash
docker build -t chatbot .
```

5. Run image
```bash
docker run -p 8501:8501 chatbot
```
