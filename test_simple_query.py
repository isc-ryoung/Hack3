"""
Simple test to query a model with the question "What is opencode?"
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(override=True)

# Configuration
api_key = os.getenv("OPENAI_API_KEY")
# model_name = "gpt-5-mini"  # Use available model on internal API
model_name = "openai/gpt-oss-120b"  # Use available model on internal API
base_url = "https://plaza.iscinternal.com/genai/v1"
question = "What is InterSystems?"

# Display configuration
print(f"API Key: {api_key}")
print(f"Model: {model_name}")
print(f"Base URL: {base_url}")
print("-" * 70)

# Initialize OpenAI client with custom base URL
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# Make a simple query
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question}
    ]
)

# Print the response
print(f"Question: {question}")
print("\nResponse:")
print(response.choices[0].message.content)
print(f"\nModel used: {response.model}")
print(f"Tokens used: {response.usage.total_tokens}")
