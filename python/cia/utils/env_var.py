import os

def get_openai_api_key() -> str:
    """Get OpenAI API key from environment variable."""
    var: str = os.environ.get("OPENAI_API_KEY", "")
    if not var:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return var
