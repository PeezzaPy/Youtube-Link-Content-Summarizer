from transformers import BartTokenizer, BartForConditionalGeneration

model_dir = "D:/TUP SCHOOLWORKS/3rd Year/ACTIVITIES/2ND SEM/AUTOMATA/PROJECT/Youtube-Link-Content-Summarizer/app/model/trained_model"
tokenizer = BartTokenizer.from_pretrained(model_dir)
model = BartForConditionalGeneration.from_pretrained(model_dir)

def summarize_transcript(text, max_length=150, min_length=10, do_sample=False):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(
        inputs['input_ids'], 
        num_beams=4, 
        max_length=max_length, 
        min_length=min_length, 
        length_penalty=2.0, 
        early_stopping=True, 
        do_sample=do_sample
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary
