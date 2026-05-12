#step2: Agent Executor
from agent import JeffAgent
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue

class JeffAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent=JeffAgent()


    async def execute(self, context:RequestContext, event_queue:EventQueue):
        query=context.get_user_input()
        context_id=context.context_id()
        response=await self.agent.get_response(query=query,context_id=context_id)
        return response["content"]


    async def cancel(self, context:RequestContext, event_queue:EventQueue):
        #logic
        return 
