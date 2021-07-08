# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:04:23 2021

@author: avina
"""

from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")
import streamlit as st


def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)
def paraphrase(phrases):
    for phrase in phrases:
        para_phrases = pp.augment(input_phrase=phrase)
        for para_phrase in para_phrases:
            return para_phrase

pp = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=True)

# paraphrase([input()])

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
        summary_result = paraphrase([message])
        st.success(summary_result)
    st.sidebar.subheader("By")
    st.sidebar.text("Avinash Nahar")
    st.sidebar.text("Adbureau Analytics ")
    st.sidebar.text(" www.adbureau.co ")
	

if __name__ == '__main__':
	main()

        

