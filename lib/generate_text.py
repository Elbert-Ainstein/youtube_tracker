from transformers import GPT2LMHeadModel, GPT2Tokenizer
from get_channel import get_channel

model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def gen():
    res = get_channel()
    for i in res[0]['items']:
        title = i['snippet']['title']
        description = i['snippet']['description']
        text = title + " " + description
        
        inputs = tokenizer.encode(text, return_tensors='pt')
        
        outputs = model.generate(inputs, max_length=100, do_sample=True)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(title)
        print(description)
        print(generated_text)
                
        return title[0]['snippet']['title'], description, generated_text
    
gen()
    