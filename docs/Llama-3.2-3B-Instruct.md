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
pip install transformers accelerate huggingface_hub --index-url https://pypi.org/simple/
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
