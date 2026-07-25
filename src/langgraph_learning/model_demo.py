from langgraph_learning.graph import create_primary_model
from pprint import pprint


def main() -> None:
    model = create_primary_model()

    response = model.invoke(
        "Reply with exactly: NVIDIA connection works.",
        thinking_mode=False,
    )

    print(response.content)
    pprint(response.usage_metadata, sort_dicts=False)
    pprint(response.response_metadata, sort_dicts=False)


if __name__ == "__main__":
    main()
