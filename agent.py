from langchain.agents import create_agent
import getpass, os

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")


def get_weather(city: str) -> str:
    return f"It's always sunny in {city}"

agent = create_agent(
    model="",
    tools = [],
    system_prompt=""
)

agent.invoke(
    {
        "messages": [{
            "role": "user", "content": "what is the weather in sf"
        }]
    }
)