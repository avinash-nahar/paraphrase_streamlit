# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:10:22 2021

@author: avina
"""

#from transformers import pipeline


import streamlit as st
# from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# import torch
# torch.cuda.empty_cache()

# model_name = 'tuner007/pegasus_paraphrase'
# torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
# torch_device = 'cpu'

# #generator = pipeline('text-generation',model='zanderbush/Paraphrase')


# tokenizer = PegasusTokenizer.from_pretrained(model_name)
# model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


# @st.cache(max_entries=10, ttl=3600)
# def generate_sentence(sentence):
#     generator(sentence, num_return_sequences=2)

@st.cache(max_entries=10, ttl=3600)
def get_response(input_text):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=60,num_beams=10, num_return_sequences=5, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text
#get_response(input())


def main():
    st.title("English Sentence Paraphrasing !")
    st.subheader("AI to improve Grammer")
    # st.markdown("""
    # 	#### Description
    # 	+ This is a Natural Language Processing(NLP) Based App useful for Artificial Intelligence to
    # 	Improve your english sentences before you upload on social media. Also we can Summarize an entire document.
    # 	""")
    message = st.text_area("Enter Text for Paraphrasing","Type here... ")
    if st.button("Paraphrase!"):
        summary_result = 'testing 1 2 3'
        st.success(summary_result)
    
    
    # st.subheader("AI to Generate Sentences for you.")
    # message2 = st.text_area("Generate Sentences","Type here... ")
    # if st.button("Generate!"):
    #     summary_result2 = get_response(message2)
    #     st.success(summary_result2)
    
    
    
    st.sidebar.subheader("By")
    st.sidebar.text("Avinash Nahar")
    st.sidebar.text("Adbureau Analytics - Pegas Version")
    st.sidebar.text(" www.adbureau.co ")
	

if __name__ == '__main__':
	main()


# Generator

# from transformers import pipeline

# generator = pipeline('text-generation',model='zanderbush/Paraphrase')




# def get_response(input_text,num_return_sequences,num_beams):
#   batch = tokenizer([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
#   translated = model.generate(**batch,max_length=60,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
#   tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#   return tgt_text

# num_beams = 10
# num_return_sequences = 5
# #context = input()
# get_response(input(),num_return_sequences,num_beams)
