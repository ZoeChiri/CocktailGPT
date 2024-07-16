import os
from apikey import apikey
#imports
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain


os.environ['OPENAI_API_KEY'] = apikey

#setting app up
st.title('🪩🍸 Cocktail Name GPT')

prompt = st.text_input('Add your prompt here')

title_template = PromptTemplate(
    input_variables = ['name'],
    template='create a cocktail name about {name}'
    
)

# llms 
llm = OpenAI(temperature=1) 
title_chain = LLMChain(llm=llm, prompt = title_template, verbose = True)
ingredient_chain = LLMChain(llm=llm, prompt = title_template, verbose = True)
sequential_chain = SimpleSequentialChain(chains = [title_chain,ingredient_chain])


#output
if prompt: 
    response = title_chain.run(topic=prompt)
    st.write(response)
    
# chain 
ingredient_template = PromptTemplate(
    input_variables = ['name'],
    template='list cocktail ingredientns based on this name NAME: {name}'
    
)
