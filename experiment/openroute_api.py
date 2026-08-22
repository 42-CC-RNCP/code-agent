from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.chat.send(
        model="gpt-4o-mini",
        messages=[
            {"content": "What is the capital of France?", "role": "user"},
        ],
        stream=False,
    )
    print(res)
