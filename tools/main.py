from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

gemini_api_key = "AIzaSyBWGYNREjwmSgTsJXeEB_Cucs28CGb1gUc"

def fetch_weather(city: str):
    """
    fetch weather according to city

    Args:
    city: str
    """


    return f"the weather in {city} is beautiful"

weather_assistant = Agent(
    name = "weather Assistant",
    instructions = "You are helpful weather Assistant provide answer by calling fetch weather tool ",
    tools = [fetch_weather]

)

external_client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-pro",
    openai_client = external_client,
)

config = RunConfig(
    model= model,
    model_provider= external_client,
    tracing_disabled= True
)

result = Runner.run_sync(weather_assistant, input= "what is weather in Karachi", run_config= config)

print("result>>>>", result.final_output)

