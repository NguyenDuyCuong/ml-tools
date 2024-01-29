from llama_cpp import Llama

llm = Llama(model_path="./models/7B/llama-model.gguf")

output = llm(
    "Q: Name the planets in the solar system? A: ", # Prompt
    max_tokens=32, # Generate up to 32 tokens
    stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
    echo=True # Echo the prompt back in the output
)

print(output)