from langchain_nvidia_ai_endpoints import ChatNVIDIA

PRIMARY_MODEL_ID = "nvidia/nemotron-3-nano-30b-a3b"


def create_primary_model() -> ChatNVIDIA:
    return ChatNVIDIA(
        model=PRIMARY_MODEL_ID,
    )
