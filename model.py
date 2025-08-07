from transformers import pipeline

pipe = pipeline("text-generation", model="./trained_model", device="mps")

print(pipe("A rectangle has a perimeter of 20 cm. If the length is 6 cm, what is the width?", max_new_tokens=200, pad_token_id=pipe.tokenizer.eos_token_id))