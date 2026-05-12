from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from tools import get_availability
import asyncio

#step1: Agent and tool
#Step2: Agent Executor
#Step3: Agent Card
#Step4: Host the Agent

memory=MemorySaver()
class JeffAgent():
    def __init__(self):
        SUPPORTED_CONTEXT_TYPES=["text","text/plain"]
   
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        self.tools =[get_availability]
        self.system_prompt= """
        You are a scheduling personal assistant for Jeff Bezos.
        Your only job is to use the 'get_availability' tool
        to answer questions on Jeff's schedule for playing badminton.
        If the question is unrelaed to scheduling, politely say you cant help.

        """
        self.graph= create_agent(
            self.model,
            tools=self.tools,
            system_prompt=self.system_prompt,
            checkpointer=memory
        )

    async def get_response(self, query,context_id):
        inputs={"messages":[("user", query)]}
        config = {"configurable":{"thread_id":context_id}}
        response =self.graph.invoke(inputs,config)
        messages=response.get("messages",[])
        ai_messages=[message.content for message in messages]
        return {"content" : ai_messages[-1]}
agent=JeffAgent()
response=asyncio.run(agent.get_response(query="Hi, Is Jeff available on 11th November 2025?",context_id=123))
print(response)