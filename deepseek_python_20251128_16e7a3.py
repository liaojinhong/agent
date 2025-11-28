from agents import Agent, Runner, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from openai import AsyncOpenAI

# 配置API客户端（请替换为你自己的API Key）
custom_client = AsyncOpenAI(base_url="https://api.qnaigc.com/v1", api_key="sk-LZtfRPRrfveFW3Q4a_13v4PKZpAGdncGp5XL6DkV")
set_default_openai_client(custom_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True) 
