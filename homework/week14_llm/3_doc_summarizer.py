# ***
# GOAL: Summarize document by using LLM's, Document Loaders, and Prompts

# LIBRARIES AND SETUP
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from IPython.display import Markdown, display

import os
import yaml
from pprint import pprint

os.environ["OPENAI_API_KEY"] = yaml.safe_load(open('credentials.yml'))['openai']

# DOCUMENT LOADER
loader = PyPDFLoader("data/NIKE-Inc-Q3FY24-OFFICIAL-Transcript.pdf")
docs = loader.load()
docs
len(docs)

# * LLM MODELA
openai_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llama_model = OllamaLLM(model="llama3.2", temperature=0)

# 1. EXPANDING WITH PROMPT TEMPLATES

prompt = """Write a concise summary of the following:
{text}

Use 3 to 7 numbered bullet points to describe key points.
"""

prompt_template = PromptTemplate.from_template(prompt)
parser = StrOutputParser()

# Joins document contents into a single {text}
def join_docs(docs):
    return {"text": "\n\n".join(getattr(d, "page_content", str(d)) for d in docs)}

joindocs = join_docs(docs)
joindocs
pprint(joindocs)

# Llama 3.2
chain = (
    join_docs
    | prompt_template
    | llama_model
    | parser
)

summary = chain.invoke(docs)  # docs can be List[Document] or List[str]
type(summary)
print(summary)
display(Markdown(summary))

# OpenAI
chain = (
    join_docs
    | prompt_template
    | openai_model
    | parser
)

summary = chain.invoke(docs)  # docs can be List[Document] or List[str]
type(summary)
print(summary)
display(Markdown(summary))


# 2. Expand prompt template
prompt = """
Write a business report from the following earnings call transcript:
{text}

Use the following Markdown format:
# Insert Descriptive Report Title

## Earnings Call Summary
Use 3 to 7 numbered bullet points

## Important Financials
Describe the most important financials discussed during the call. Use 3 to 5 numbered bullet points.

## Key Business Risks
Describe any key business risks discussed on the call. Use 3 to 5 numbered bullets.

## Conclusions
Conclude with any overaching business actions that the company is pursuing that may have a positive or negative implications and what those implications are. 

"""

prompt_template = PromptTemplate.from_template(prompt)
output_parser = StrOutputParser()

# Llama 3.2
chain = (
    join_docs
    | prompt_template
    | llama_model
    | output_parser
)

summary = chain.invoke(docs)  # docs can be List[Document] or List[str]
print(summary)
display(Markdown(summary))


# OpenAI
chain = (
    join_docs
    | prompt_template
    | openai_model
    | output_parser
)

summary = chain.invoke(docs)  # docs can be List[Document] or List[str]
print(summary)
display(Markdown(summary))