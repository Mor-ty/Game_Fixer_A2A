# Step3: Agent Card
from a2a.types import (
    AgentCard,
    AgentCapabilities,
    AgentInterface,
    AgentSkill,
)
from a2a.utils.constants import DEFAULT_RPC_URL, PROTOCOL_VERSION_CURRENT, TransportProtocol

from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import create_agent_card_routes, create_jsonrpc_routes
from a2a.server.tasks import InMemoryTaskStore
from agent_executor import MarkAgentExecutor
from starlette.applications import Starlette
import uvicorn


def main(host: str = "localhost", port: int = 10005) -> None:
    base_url = f"http://{host}:{port}"
    skill = AgentSkill(
        id="schedule-mark",
        name="Mark's Agent",
        description="Helps with finding Mark's availability with badminton",
        tags=["scheduling", "badminton"],
        examples=["Are you free to play badminton on 8th November 2025?"],
    )

    agent_card = AgentCard(
        name="MarkAgent",
        description="Helps with scheduling badminton games",
        version="1.0.0",
        capabilities=AgentCapabilities(),
        skills=[skill],
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        supported_interfaces=[
            AgentInterface(
                url=base_url,
                protocol_binding=TransportProtocol.JSONRPC,
                protocol_version=PROTOCOL_VERSION_CURRENT,
            )
        ],
    )

    request_handler = DefaultRequestHandler(
        agent_executor=MarkAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )

    routes = [
        *create_agent_card_routes(agent_card),
        *create_jsonrpc_routes(request_handler, DEFAULT_RPC_URL),
    ]
    app = Starlette(routes=routes)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()