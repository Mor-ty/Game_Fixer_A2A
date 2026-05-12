#step2: Agent Executor
from agent import MarkAgent
from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue

class MarkAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent=MarkAgent()


    async def execute(self, context:RequestContext, event_queue:EventQueue):
        query=context.get_user_input()
        context_id=context.context_id()
        response=await self.agent.invoke(query=query)
        return response


    async def cancel(self, context:RequestContext, event_queue:EventQueue):
        #logic
        return 
