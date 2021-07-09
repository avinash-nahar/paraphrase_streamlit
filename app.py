
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

torch.cuda.empty_cache()


def set_seed(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

set_seed(42)


model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")
tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  



def para2(sentence):
    text =  "paraphrase: " + sentence + " </s>"

    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
    input_ids = encoding["input_ids"]
    attention_masks = encoding["attention_mask"]
    
    outputs = model.generate(
        input_ids=input_ids, 
        attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=200,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=5
    )
    lines =[]
    for output in outputs:
        line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
        lines.append(line)
        
    return lines

def main():
    st.title("English Sentence Paraphrasing !")
    st.subheader("AI to improve your english and grammer, On the Go..")
    # st.markdown("""
    # 	#### Description
    # 	+ This is a Natural Language Processing(NLP) Based App useful for Artificial Intelligence to
    # 	Improve your english sentences before you upload on social media. Also we can Summarize an entire document.
    # 	""")
    message = st.text_area("Enter Text for Paraphrasing","Type here... ")
    if st.button("Paraphrase!"):
        summary_result = para2(message)
        st.success(summary_result)
    st.sidebar.subheader("By")
    st.sidebar.text("Avinash Nahar")
    st.sidebar.text("Adbureau Analytics ")
    st.sidebar.text(" www.adbureau.co ")
	

if __name__ == '__main__':
	main()

        
