from dotenv import load_dotenv
load_dotenv(".env.local")

"""Main entry point for the ecommerce voicebot agent."""
from src.agent import entrypoint
from livekit import agents


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
