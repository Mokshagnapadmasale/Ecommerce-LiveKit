import os 
import asyncio
from dotenv import load_dotenv
load_dotenv()

from langchain_mcp_adapters.client import MultiServerMCPClient

from openai.types import realtime

from prompts import ECOMMERCE_GREET_INSTRUCTIONS,ECOMMERCE_INSTRUCTIONS


from livekit import agents,rtc
from livekit.plugins import (
    openai,
    google,
    silero,
    turn_detector,
    noise_cancellation
)
from livekit.agents import (
    room_io,
    JobContext,
    Agent,
    AgentServer,
    AgentSession,
    mcp
)




class EcommerceAssistant(Agent):
    def __init__(self):
        super().__init__(instructions=ECOMMERCE_INSTRUCTIONS)

server = AgentServer()

@server.rtc_session()
async def voice_agent(ctx:JobContext):

    session = AgentSession(
        llm = openai.realtime.RealtimeModel(
            model="gpt-4o-realtime-preview",
            voice="coral",
            temperature=1.0,
            api_key=os.getenv('OPENAI_API_KEY'),
            input_audio_transcription=realtime.AudioTranscription(
                model="gpt-4o-mini-transcribe-2025-12-15",
                language='en'
            ),
            input_audio_noise_reduction="near_field",
            turn_detection=realtime.realtime_audio_input_turn_detection.SemanticVad(
                type="semantic_vad",
                create_response=True,
                eagerness="medium",
                interrupt_response=False
            )
            
        ),
        mcp_servers=[mcp.MCPServerHTTP(url='http://localhost:8000/sse')]
    )

    await session.start(
        room=ctx.room,
        agent=EcommerceAssistant(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=lambda params : noise_cancellation.BVCTelephony() if params.participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP else noise_cancellation.BVC(),
            ),
        ),
    )

    await session.generate_reply(
        instructions=ECOMMERCE_GREET_INSTRUCTIONS
    )

if __name__ == "__main__":
    agents.cli.run_app(server=server)