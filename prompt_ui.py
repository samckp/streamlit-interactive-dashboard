import streamlit as st 
import pandas as pd

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

# create an LLM by instantiating OpenAI object, and passing API token
llm = OpenAI(api_token="sk")

# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

st.title("Prompt-driven data analysis with PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    # new code below...
    prompt = st.text_area("Enter your prompt:")

     # Generate output
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("Please enter a prompt.")

