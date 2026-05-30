from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
import yaml
import os

output_parser = StrOutputParser()

########## ollama ###################################
# OllamaLM - designed for text completion (single prompt -> single response)
# ChatOllama - designed for chat completion (multi-turn conversations with roles
# like system, user/human, assistant/ai)

# Llama 3.2 model

# Temperature is a parameter that controls the level of randomness or
# creativity in the LLM model output. Range is typically 0-1. 
# Some implementations range is 0-2
# Low temperature - more deterministic and focused
# high temperature - more random and creative
# ChatOllama temperature range 0-1 default=0
# ChatOpenAI temperature range 0-2 default=0.7

# chatollama

llama_chat_model = ChatOllama(model="llama3.2")
messages = [
    SystemMessage(content="Translate the following from English into French"),
    HumanMessage(content="hi!"),
]


# 1. model, parser
ai_msg = llama_chat_model.invoke(messages)
type(ai_msg)
ai_msg

# print langchain AIMessage
print(ai_msg.content)

# parse AIMessage
output_parser.invoke(ai_msg)

# function chain
output_parser.invoke(llama_chat_model.invoke(messages))

# 2. chain
chain = llama_chat_model | output_parser
chain.invoke(messages)


# 3. prompt templates
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "Translate the following into {language}"), ("human", "{text}")]
)

chain = prompt_template | llama_chat_model | output_parser
chain.invoke({"language": "french", "text": "hi"})

# 4. RunnablePassThrough
from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough() | prompt_template | llama_chat_model | output_parser

chain.invoke({"language": "french", "text": "hi"})


############### OpenAI ############################

os.environ["OPENAI_API_KEY"] = yaml.safe_load(open('credentials.yml'))['openai']



# ChatOpenAI MODEL
openai_chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=1.0)

messages = [
    SystemMessage(content="Translate the following from English into French"),
    HumanMessage(content="hi!"),
]

# 1. model, parser
ai_msg = openai_chat_model.invoke(messages)
ai_msg
output_parser.invoke(ai_msg)

# function chain
output_parser.invoke(openai_chat_model.invoke(messages))

# 2. chain
chain = openai_chat_model | output_parser
chain.invoke(messages)

# 3. prompt templates
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "Translate the following into {language}"), ("human", "{text}")]
)

chain = prompt_template | openai_chat_model | output_parser
chain.invoke({"language": "french", "text": "hi"})

# 4. RunnablePassThrough
from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough() | prompt_template | openai_chat_model | output_parser

chain.invoke({"language": "french", "text": "hi"})