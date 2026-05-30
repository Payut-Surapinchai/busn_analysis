# Import the necessary libraries for this homework
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from IPython.display import Markdown, display

# Document Loader
loader = TextLoader("homework/NVDA_2025Q2.txt")
docs = loader.load()

# Check if the contents in the .txt file were loaded properly
docs

# Initiate a llama model
llama_model = OllamaLLM(model="llama3.2", temperature=0)

# Create a prompt
prompt = """
Write a business report from the following earnings call transcript:
{text}

Use the following Markdown format:

# Insert Report title as NVIDIA Q4 FY2023 Earnings Call Highlights

## Financial Highlights

Use 3 bullet points to summarize the Year-over-Year and the total of Revenue, GAAP EPS and Non-GAAP EPS, using only numbers.

## Segment Highlights

Describe the most important Year-over-Year highlights segments in 3 bullet points.

## Cash Flow and Capex

Use 3 bullet points to summarize the Year-over-Year and the total of Operating cash flow, Capital Expenditures, and Cash and equivalents, using only numbers.

## Strategic Moves

Use 3 bullet points to summarize the announcements, or strategic moves from the earnings call transcript.

## Key Risks

Use 3 bullet points to summarize the key risks discussed on the call.

"""

# Put the prompt in the PromptTemplate to create a promp template for the llama model
prompt_template = PromptTemplate.from_template(prompt)

# Initiate a string parser to extract plain text
parser = StrOutputParser()

# Chain the actions together (similar to piping in R)
# Gives the final prompt to llama model -> llama model reads the prompt and generate text -> extracts plain text
chain = prompt_template | llama_model | parser

# Store the output from the chain invoke in summary
summary = chain.invoke({"text": prompt})

# Display the result in a Markdown format
display(Markdown(summary))