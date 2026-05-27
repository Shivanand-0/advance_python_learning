from datasets import Dataset
from transformers import ( 
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    TrainingArguments, 
    Trainer,
    DataCollatorWithPadding # FIX 1: Import the data collator
) 

data = { 
    "text": [ "The movie was absolutely fantastic, I loved every minute of it!", 
              "I am so disappointed with the service I received today.", 
              "An incredible experience that I would highly recommend to everyone.", 
              "The food was bland and the atmosphere was even worse.", 
              "What a brilliant performance by the lead actor!", 
              "I've never been so bored during a presentation in my life.", 
              "The interface is intuitive and makes the job so much easier.", 
              "Total waste of money, do not buy this product.", 
              "The sunset at the beach was breathtakingly beautiful.", 
              "The delivery was late and the packaging was completely damaged." ], 
    "labels": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 
} 

dataset = Dataset.from_dict(data) 

model_name = "distilbert-base-uncased" 
tokenizer = AutoTokenizer.from_pretrained(model_name) 

def tokenize_fxn(data): 
    return tokenizer( 
        data["text"], 
        truncation=True, 
    ) 

# FIX 2: Added remove_columns=["text"] to drop the raw strings after tokenization
tokenized_dataset = dataset.map(tokenize_fxn, batched=True, remove_columns=["text"]) 

# step4 load model 
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2) 

# step5 Training Arguments 
training_args = TrainingArguments( 
    output_dir="./result", 
    num_train_epochs=3, 
    per_device_train_batch_size=2, 
    logging_steps=1, 
    save_strategy="epoch" 
) 

# FIX 3: Initialize the data collator to handle dynamic batch padding
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# 6. Initialize Trainer 
trainer = Trainer( 
    model=model, 
    args=training_args, 
    train_dataset=tokenized_dataset, 
    data_collator=data_collator # FIX 4: Pass the collator here
) 

# 7. Start training 
trainer.train() 

model.save_pretrained("./fine_tuned_model") 
tokenizer.save_pretrained("./fine_tuned_model") 

print("finetuned successfully!!")
