import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

def generate_response(prompt: str, context: str) -> str:
    BASE_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
    ADAPTER_DIR = "./domain_llm_output"

    tokenizer = AutoTokenizer.from_pretrained(ADAPTER_DIR)
    
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )

    # Load Base
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto"
    )
    
    # Merge Adapter weights
    model = PeftModel.from_pretrained(base_model, ADAPTER_DIR)
    model.eval()

    # Reconstruct the template format used during training
    formatted_prompt = (
        f"<|im_start|>system\nYou are a domain expert assistant in Finance and Technology.<|im_end|>\n"
        f"<|im_start|>context\nTopic: {context}<|im_end|>\n"
        f"<|im_start|>user\n{prompt}<|im_end|>\n"
        f"<|im_start|>assistant\n"
    )

    inputs = tokenizer(formatted_prompt, return_tensors="pt").to("cuda")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs, 
            max_new_tokens=150, 
            temperature=0.3, # Lower values produce less erratic, more professional language
            eos_token_id=tokenizer.eos_token_id
        )
    
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=False)
    # Extract structural assistant text response
    return decoded.split("<|im_start|>assistant\n")[-1].replace("<|im_end|>", "").strip()

# Example Test Case
if __name__ == "__main__":
    user_q = "What are the core components required to set up a production-ready CI/CD pipeline for microservices running on Docker?"
    topic = "Technology - DevOps"
    
    print("\n--- Generating Fine-Tuned Model Response ---")
    response = generate_response(user_q, topic)
    print(response)
