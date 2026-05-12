from google.adk import Agent
import httpx
from dotenv import load_dotenv
from a2a.client import A2ACardResolver
from a2a.client import A2AClient
from a2a.types import AgentCard, SendMessageRequest, SendMessageResponse
load_dotenv()

class RemoteAgentConnection():
    """
    Represents a single connection between the Host Agent and one remote agent.

    Each connection wraps the A2AClient, which knows how to send messages to that agent over HTTP.
    """
    def __init__(self, agent_card: AgentCard, agent_url: str):
        self.agent_card = agent_card
        self.agent_url = agent_url
        self.http_client = httpx.AsyncClient(timeout=30)
        self.client = A2AClient(slef.http_client,agent_card,url=agent_url)
    async def send_message(self, message_request: SendMessageRequest) -> SendMessageResponse:
        """Send a message to this remote agent."""
        return await self.client.send_message(message_request)


class ElonAgent()
    def __init__(self):
        self.remote_agents_urls=remote_agents_urls or []
        self.agent=None

    async def create_agent(self):
        self.agent=Agent(
            model="gemini-2.5-flash",
            name="Elon_Agent",
            description="Helps coordinate badminton games with friends",
            instruction="You are Elon's personal agent, you help to organize games with friends",
            tools=[]
        )
        return self.agent
    async def _load_remote_agents():
        async with httpx.AsyncClient(timeout=30) as client:
            for url in self.remote_agent_urls:
                resolver=A2ACardResolver(client,url)
                card=await resolver.get_agent_card()
                

root_agent=agent