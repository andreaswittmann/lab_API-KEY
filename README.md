# BigModel API Test Program

A simple Python test program to verify usage of the BigModel API. It uses the `glm-4.6` model to ask "Hello, what is your name and who created you?" and prints the response.

## Prerequisites

- Python 3.x
- Virtual environment (recommended)
- OpenAI Python library

## Setup

1. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install openai
   ```

3. Set the API key environment variable:
   ```
   export ZHIPU_AI_API_KEY=your_api_key_here
   ```

## Usage

Run the test program:
```
python3 test_bigmodel.py
```

The program will make an API call to BigModel and print the model's response.

## GitHub Actions

This project includes a GitHub Actions workflow that automatically tests the BigModel API integration.

### Setting up the workflow

1. In your GitHub repository, go to Settings > Secrets and variables > Actions
2. Add a new repository secret named `ZHIPU_AI_API_KEY` with your BigModel API key
3. The workflow will run on pushes and pull requests to the main branch
4. Check the Actions tab to see the workflow results