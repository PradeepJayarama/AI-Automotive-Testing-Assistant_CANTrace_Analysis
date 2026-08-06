import asyncio
from copilot import CopilotClient
from copilot.session_events import AssistantMessageData, SessionIdleData
from copilot.session import PermissionHandler


def explain_failure(Data):
    async def main():
        ai_result = ""

        async with CopilotClient() as client:
            async with await client.create_session(
                on_permission_request=PermissionHandler.approve_all,
                model="auto",
                # or "gpt-5", "claude-sonnet-4.5", etc.
                # provider={"type": "openai",
                #           "base_url": "https://models.github.ai/inference",
                #           "api_key": os.getenv("GITHUB_TOKEN")}
            ) as session:
                done = asyncio.Event()

                def on_event(event):
                    nonlocal ai_result
                    match event.data:
                        case AssistantMessageData() as data:
                            ai_result = data.content  # generated response
                        case SessionIdleData():
                            done.set()  # signals the session is done

                session.on(on_event)
                prompt = f"""
You are an Automotive Validation Engineer.

Analyze these abnormal CAN frames.

{Data}

Explain:

1. Possible root causes

2. Recommended tests

3. Severity
"""
                await session.send(prompt)
                await done.wait()

        return ai_result

    return asyncio.run(main())

