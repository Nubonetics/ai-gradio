# `ai-gradio`

A Python package that makes it easy for developers to create machine learning apps powered by OpenAI and Google's Gemini models.

## Installation

You can install `ai-gradio` with different providers:

```bash
# Install with OpenAI support
pip install 'ai-gradio[openai]'

# Install with Gemini support  
pip install 'ai-gradio[gemini]'

# Install with all providers
pip install 'ai-gradio[all]'
```

## Basic Usage

First, set your API key in the environment:

For OpenAI:
```bash
export OPENAI_API_KEY=<your token>
```

For Gemini:
```bash
export GEMINI_API_KEY=<your token>
```

Then in a Python file:

```python
import gradio as gr
from ai_gradio import registry

# Create a Gradio interface
interface = gr.load(
    name='gpt-4-turbo',  # or 'gemini-pro' for Gemini
    src=registry,
    title='AI Chat',
    description='Chat with an AI model'
).launch()
```

## Features

### Text Chat
Basic text chat is supported for all models. The interface provides a chat-like experience where you can have conversations with the AI model.

### Voice Chat (OpenAI only)
Voice chat is supported for OpenAI models. You can enable it by setting `enable_voice=True`:

```python
interface = gr.load(
    name='gpt-4-turbo',
    src=registry,
    enable_voice=True
).launch()
```

### Video Chat (Gemini only)
Video chat is supported for Gemini models. You can enable it by setting `enable_video=True`:

```python
interface = gr.load(
    name='gemini-pro',
    src=registry,
    enable_video=True
).launch()
```

### Customization

You can customize the interface by adding examples, changing the title, or adding a description:

```python
interface = gr.load(
    name='gpt-4-turbo',
    src=registry,
    title='Custom AI Chat',
    description='Chat with an AI assistant',
    examples=[
        "Explain quantum computing to a 5-year old",
        "What's the difference between machine learning and AI?"
    ]
).launch()
```

### Composition

You can combine multiple models in a single interface using Gradio's Blocks:

```python
import gradio as gr
from ai_gradio import registry

with gr.Blocks() as demo:
    with gr.Tab("GPT-4"):
        gr.load('gpt-4-turbo', src=registry)
    with gr.Tab("Gemini"):
        gr.load('gemini-pro', src=registry)

demo.launch()
```

## Supported Models

### OpenAI Models
- gpt-4-turbo
- gpt-4
- gpt-3.5-turbo

### Gemini Models
- gemini-pro
- gemini-pro-vision

## Requirements

- Python 3.10 or higher
- gradio >= 5.9.1

Additional dependencies are installed based on your chosen provider:
- OpenAI: `openai>=1.58.1`
- Gemini: `google-generativeai`

## Troubleshooting

If you get a 401 authentication error, make sure your API key is properly set. You can set it manually in your Python session:

```python
import os

# For OpenAI
os.environ["OPENAI_API_KEY"] = "your-api-key"

# For Gemini
os.environ["GEMINI_API_KEY"] = "your-api-key"
```

## Optional Dependencies

For voice chat functionality:
- gradio-webrtc
- numba==0.60.0
- pydub

For video chat functionality:
- opencv-python
- Pillow