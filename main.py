import pydantic

ExampleType = pydantic.Json[dict[str, str]]
