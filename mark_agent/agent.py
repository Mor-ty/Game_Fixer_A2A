from crewai import LLM, Agent, Crew, Process, Task
from dotenv import load_dotenv
import os
load_dotenv()
from tools import AvailabilityTool
api_key=os.getenv("GOOGLE_API_KEY")
class MarkAgent():
    def __init__(self):
        self.api_key=os.getenv("GOOGLE_API_KEY")
        self.llm=LLM(
            model="gemini-2.5-flash",
            api_key=self.api_key,
        )

        self.agent = Agent(
                role="Scheduling Assistant",
                goal="Answer questions about Mark's availability using the calendar tool",
                backstory="You only answer scheduling questions and you always use the calendar tool",
                tools=[AvailabilityTool()],
                llm=self.llm,
            )
    async def invoke(self,user_question):
        task=Task(
            description=f"User asked:'{user_question}'.",
            expected_output="Polite response about availability.",
            agent=self.agent,
        )
        crew= Crew(
            agent=[self.agent],
            tasks=[task],
            process=Process.sequential,

        )
        agent_response=str(crew.kickoff())
        return agent_response
# mark_agent=MarkAgent()
# import asyncio
# print(asyncio.run(mark_agent.invoke("hi, is Mark available on 8th November 2025)")))

