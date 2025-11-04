# Plan for BigModel API Test Program

## Overview
Create a small Python test program to verify BigModel API usage. The program will:
- Use API key from environment variable `ZHIPU_AI_API_KEY`
- Call the `glm-4.6` model
- Ask: "Hello, what is your name and who created you?"
- Print the response

## API Details
- Base URL: `https://open.bigmodel.cn/api/paas/v4`
- Compatible with OpenAI API format
- Authentication: Bearer token with API key

## Todo List
1. **Set up Python script structure**: Create a new Python file (e.g., `test_bigmodel.py`) with necessary imports (os, openai).
2. **Configure API client**: Initialize OpenAI client with custom base_url and API key from environment.
3. **Implement API call**: Create a chat completion request with the specified model and user message.
4. **Handle response**: Print the assistant's response to the console.
5. **Add error handling**: Include basic try-except for API errors or missing environment variables.
6. **Test the program**: Ensure it runs without syntax errors and handles the API interaction correctly.

## Implementation Notes
- Use the `openai` Python library for API calls (install via `pip install openai` if needed).
- The API is OpenAI-compatible, so standard chat completion methods can be used.
- Keep the program simple and focused on the test functionality.