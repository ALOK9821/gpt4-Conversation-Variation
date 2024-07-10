# GPT-4 and GroQ (Llama) Conversation Variation Generator

Welcome to the GPT-4 and GroQ (Llama) Conversation Variation Generator project! This repository contains a script that uses both GPT-4 (OpenAI) and GroQ (Llama) models to generate variations of conversations from provided Jupyter notebooks (.ipynb files).

## Introduction
This project was developed as part of a coding assignment. The goal is to generate variations of RLHF (Reinforcement Learning from Human Feedback) conversations, maintaining the flow and meaning while providing rephrased interactions between the assistant and the user.

## Features
- **Dual Model Support:** Use either GPT-4 from OpenAI or GroQ (Llama) models for generating variations.
- **Flexible Input/Output:** Specify input and output paths for Jupyter notebook files.
- **Environment Variable Management:** Securely manage API keys using a .env file.

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Required Packages
Install the required packages using pip:
```bash
pip install openai
pip install groq
pip install python-dotenv
```
### Environment Variables
```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```
### Running the Project
- Set the input and output paths for your Jupyter notebook files in `main.py` (lines 27-28).
- Execute the `main.py`

### Model Control
- By default, the project uses the `GroQ` model for local testing. You can switch to `GPT-4` by modifying the function call in `main.py`
```
  variation = generate_variation(prompt, model='gpt')
```

