from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Team-ACE/ToolACE-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype='auto',
    device_map='auto'
)

print("Model and tokenizer loaded successfully!")
