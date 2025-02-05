from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
groq_api_key=os.getenv("groq_api_key")
model=ChatGroq(model="Llam3.1",groq_api_key=groq_api_key)
system_template="Translate the following into {language}"
prompt=ChatPromptTemplate.from_messages([('system',system_template),('user','{text}')])
parser=StrOutputParser()
chain=prompt|model|parser
app=FastAPI(title="Langchain server",version="1.0",description="A simple api server using Langchain runnable interfaces")
add_routes(app,chain,path='/chain')
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)