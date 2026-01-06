from langchain.agents import create_agent

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