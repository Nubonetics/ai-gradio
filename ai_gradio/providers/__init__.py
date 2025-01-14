import gradio as gr

def custom_load(name: str, src: dict, **kwargs):
    # Only use custom loading if name contains provider prefix
    if ':' in name:
        provider, model = name.split(':')
        # Create provider-specific model key
        model_key = f"{provider}:{model}"
        
        if model_key not in src:
            available_models = [k for k in src.keys()]
            raise ValueError(f"Model {model_key} not found. Available models: {available_models}")
        return src[model_key](name=model, **kwargs)
    
    # Fall back to original gradio behavior if no provider prefix
    return original_load(name, src, **kwargs)

# Store original load function before overriding
original_load = gr.load
gr.load = custom_load

registry = {}


try:
    from .openai_gradio import registry as openai_registry
    registry.update({f"openai:{k}": openai_registry for k in [
        "gpt-4o-2024-11-20",
        "gpt-4o",
        "gpt-4o-2024-08-06",
        "gpt-4o-2024-05-13",
        "chatgpt-4o-latest",
        "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18",
        "o1-preview",
        "o1-preview-2024-09-12",
        "o1-mini",
        "o1-mini-2024-09-12",
        "gpt-4-turbo",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-turbo-preview",
        "gpt-4-0125-preview",
        "gpt-4-1106-preview",
        "gpt-4",
        "gpt-4-0613",
        "o1-2024-12-17",
        "gpt-4o-realtime-preview-2024-10-01",
        "gpt-4o-realtime-preview",
        "gpt-4o-realtime-preview-2024-12-17",
        "gpt-4o-mini-realtime-preview",
        "gpt-4o-mini-realtime-preview-2024-12-17",
    ]})
except ImportError:
    pass

try:
    from .gemini_gradio import registry as gemini_registry
    registry.update({f"gemini:{k}": gemini_registry for k in [
        'gemini-1.5-flash',
        'gemini-1.5-flash-8b',
        'gemini-1.5-pro',
        'gemini-exp-1114',
        'gemini-exp-1121',
        'gemini-exp-1206',
        'gemini-2.0-flash-exp',
        'gemini-2.0-flash-thinking-exp-1219'
    ]})
except ImportError:
    pass

try:
    from .crewai_gradio import registry as crewai_registry
    # Add CrewAI models with their own prefix
    registry.update({f"crewai:{k}": crewai_registry for k in ['gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo']})
except ImportError:
    pass

try:
    from .anthropic_gradio import registry as anthropic_registry
    registry.update({f"anthropic:{k}": anthropic_registry for k in [
        'claude-3-5-sonnet-20241022',
        'claude-3-5-haiku-20241022',
        'claude-3-opus-20240229',
        'claude-3-sonnet-20240229',
        'claude-3-haiku-20240307',
    ]})
except ImportError:
    pass

try:
    from .lumaai_gradio import registry as lumaai_registry
    registry.update({f"lumaai:{k}": lumaai_registry for k in [
        'dream-machine',
        'photon-1',
        'photon-flash-1'
    ]})
except ImportError:
    pass

try:
    from .xai_gradio import registry as xai_registry
    registry.update({f"xai:{k}": xai_registry for k in [
        'grok-beta',
        'grok-vision-beta'
    ]})
except ImportError:
    pass

try:
    from .cohere_gradio import registry as cohere_registry
    registry.update({f"cohere:{k}": cohere_registry for k in [
        'command-r7b-12-2024',
        'command-light',
        'command-nightly',
        'command-light-nightly'
    ]})
except ImportError:
    pass

try:
    from .sambanova_gradio import registry as sambanova_registry
    registry.update({f"sambanova:{k}": sambanova_registry for k in [
        'Meta-Llama-3.1-405B-Instruct',
        'Meta-Llama-3.1-8B-Instruct',
        'Meta-Llama-3.1-70B-Instruct',
        'Meta-Llama-3.1-405B-Instruct-Preview',
        'Meta-Llama-3.1-8B-Instruct-Preview',
        'Meta-Llama-3.3-70B-Instruct',
        'Meta-Llama-3.2-3B-Instruct',
    ]})
except ImportError:
    pass

try:
    from .hyperbolic_gradio import registry as hyperbolic_registry
    registry.update({f"hyperbolic:{k}": hyperbolic_registry for k in [
        'Qwen/Qwen2.5-Coder-32B-Instruct',
        'meta-llama/Llama-3.2-3B-Instruct',
        'meta-llama/Meta-Llama-3.1-8B-Instruct',
        'meta-llama/Meta-Llama-3.1-70B-Instruct',
        'meta-llama/Meta-Llama-3-70B-Instruct',
        'NousResearch/Hermes-3-Llama-3.1-70B',
        'Qwen/Qwen2.5-72B-Instruct',
        'deepseek-ai/DeepSeek-V2.5',
        'meta-llama/Meta-Llama-3.1-405B-Instruct',
        'Qwen/QwQ-32B-Preview',
        'meta-llama/Llama-3.3-70B-Instruct',
        'deepseek-ai/DeepSeek-V3'
    ]})
except ImportError:
    pass

try:
    from .qwen_gradio import registry as qwen_registry
    registry.update({f"qwen:{k}": qwen_registry for k in [
        "qwen-turbo-latest",
        "qwen-turbo",
        "qwen-plus",
        "qwen-max",
        "qwen1.5-110b-chat",
        "qwen1.5-72b-chat",
        "qwen1.5-32b-chat",
        "qwen1.5-14b-chat",
        "qwen1.5-7b-chat",
        "qwq-32b-preview",
        'qvq-72b-preview'
    ]})
except ImportError:
    pass

try:
    from .fireworks_gradio import registry as fireworks_registry
    registry.update({f"fireworks:{k}": fireworks_registry for k in [
        'whisper-v3',
        'whisper-v3-turbo',
        'f1-preview',
        'f1-mini'
    ]})
except ImportError:
    pass

try:
    from .together_gradio import registry as together_registry
    registry.update({f"together:{k}": together_registry for k in [
        # Vision Models
        'meta-llama/Llama-Vision-Free',
        'meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo',
        'meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo',
        
        # Llama 3 Series
        'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
        'meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo',
        'meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo',
        'meta-llama/Meta-Llama-3-8B-Instruct-Turbo',
        'meta-llama/Meta-Llama-3-70B-Instruct-Turbo',
        'meta-llama/Llama-3.2-3B-Instruct-Turbo',
        'meta-llama/Meta-Llama-3-8B-Instruct-Lite',
        'meta-llama/Meta-Llama-3-70B-Instruct-Lite',
        'meta-llama/Llama-3-8b-chat-hf',
        'meta-llama/Llama-3-70b-chat-hf',
        'meta-llama/Llama-3.3-70B-Instruct-Turbo',
        
        # Other Large Models
        'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
        'Qwen/Qwen2.5-Coder-32B-Instruct',
        'microsoft/WizardLM-2-8x22B',
        'databricks/dbrx-instruct',
        
        # Gemma Models
        'google/gemma-2-27b-it',
        'google/gemma-2-9b-it',
        'google/gemma-2b-it',
        
        # Mixtral Models
        'mistralai/Mixtral-8x7B-Instruct-v0.1',
        'mistralai/Mixtral-8x22B-Instruct-v0.1',
        
        # Qwen Models
        'Qwen/Qwen2.5-7B-Instruct-Turbo',
        'Qwen/Qwen2.5-72B-Instruct-Turbo',
        'Qwen/Qwen2-72B-Instruct',
        
        # Other Models
        'deepseek-ai/deepseek-llm-67b-chat',
        'Gryphe/MythoMax-L2-13b',
        'meta-llama/Llama-2-13b-chat-hf',
        'mistralai/Mistral-7B-Instruct-v0.1',
        'mistralai/Mistral-7B-Instruct-v0.2',
        'mistralai/Mistral-7B-Instruct-v0.3',
        'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO',
        'togethercomputer/StripedHyena-Nous-7B',
        'upstage/SOLAR-10.7B-Instruct-v1.0'
    ]})
except ImportError:
    pass

try:
    from .deepseek_gradio import registry as deepseek_registry
    registry.update({f"deepseek:{k}": deepseek_registry for k in [
        'deepseek-chat',
        'deepseek-coder',
        'deepseek-vision'
    ]})
except ImportError:
    pass

try:
    from .smolagents_gradio import registry as smolagents_registry
    registry.update({f"smolagents:{k}": smolagents_registry for k in [
        'Qwen/Qwen2.5-72B-Instruct',
        'Qwen/Qwen2.5-4B-Instruct',
        'Qwen/Qwen2.5-1.8B-Instruct',
        'meta-llama/Llama-3.3-70B-Instruct',
        'meta-llama/Llama-3.1-8B-Instruct'
    ]})
except ImportError:
    pass

try:
    from .groq_gradio import registry as groq_registry
    registry.update({f"groq:{k}": groq_registry for k in [
        "llama3-groq-8b-8192-tool-use-preview",
        "llama3-groq-70b-8192-tool-use-preview",
        "llama-3.2-1b-preview",
        "llama-3.2-3b-preview",
        "llama-3.2-11b-vision-preview",
        "llama-3.2-90b-vision-preview",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "gemma-7b-it",
        "llama-3.3-70b-versatile",
        "llama-3.3-70b-specdec"
    ]})
except ImportError:
    pass

try:
    from .browser_use_gradio import registry as browser_use_registry
    registry.update({f"browser:{k}": browser_use_registry for k in [
        "gpt-4o-2024-11-20",
        "gpt-4o",
        "gpt-4o-2024-08-06",
        "gpt-4o-2024-05-13",
        "chatgpt-4o-latest",
        "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18",
        "o1-preview",
        "o1-preview-2024-09-12",
        "o1-mini",
        "o1-mini-2024-09-12",
        "gpt-4-turbo",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-turbo-preview",
        "gpt-4-0125-preview",
        "gpt-4-1106-preview",
        "gpt-4",
        "gpt-4-0613",
        "o1-2024-12-17",
        "gpt-4o-realtime-preview-2024-10-01",
        "gpt-4o-realtime-preview",
        "gpt-4o-realtime-preview-2024-12-17",
        "gpt-4o-mini-realtime-preview",
        "gpt-4o-mini-realtime-preview-2024-12-17",
        "gpt-3.5-turbo"
    ]})
except ImportError:
    pass

try:
    from .swarms_gradio import registry as swarms_registry
    registry.update({f"swarms:{k}": swarms_registry for k in [
        'gpt-4-turbo',
        'gpt-4o-mini',
        'gpt-4',
        'gpt-3.5-turbo'
    ]})
except ImportError:
    pass

try:
    from .transformers_gradio import registry as transformers_registry
    registry.update({f"transformers:{k}": transformers_registry for k in [
        "phi-4",
        "tulu-3",
        "olmo-2-13b",
        "smolvlm",
        "moondream",
        # Add other default transformers models here
    ]})
except ImportError:
    pass

try:
    from .jupyter_agent import registry as jupyter_registry
    registry.update({f"jupyter:{k}": jupyter_registry for k in [
        'meta-llama/Llama-3.2-3B-Instruct',
        'meta-llama/Llama-3.1-8B-Instruct', 
        'meta-llama/Llama-3.1-70B-Instruct'
    ]})
except ImportError:
    pass

try:
    from .langchain_gradio import registry as langchain_registry
    registry.update({f"langchain:{k}": langchain_registry for k in [
        'gpt-4-turbo',
        'gpt-4',
        'gpt-3.5-turbo',
        'gpt-3.5-turbo-0125'
    ]})
except ImportError as e:
    print(f"Failed to import LangChain registry: {e}")
    # Optionally add more detailed error handling here

try:
    from .mistral_gradio import registry as mistral_registry
    registry.update({f"mistral:{k}": mistral_registry for k in [
        "mistral-large-latest",
        "pixtral-large-latest",
        "ministral-3b-latest",
        "ministral-8b-latest",
        "mistral-small-latest",
        "codestral-latest",
        "mistral-embed",
        "mistral-moderation-latest",
        "pixtral-12b-2409",
        "open-mistral-nemo",
        "open-codestral-mamba",
    ]})
except ImportError:
    pass

if not registry:
    raise ImportError(
        "No providers installed. Install with either:\n"
        "pip install 'ai-gradio[openai]' for OpenAI support\n"
        "pip install 'ai-gradio[gemini]' for Gemini support\n"
        "pip install 'ai-gradio[crewai]' for CrewAI support\n"
        "pip install 'ai-gradio[anthropic]' for Anthropic support\n"
        "pip install 'ai-gradio[lumaai]' for LumaAI support\n"
        "pip install 'ai-gradio[xai]' for X.AI support\n"
        "pip install 'ai-gradio[cohere]' for Cohere support\n"
        "pip install 'ai-gradio[sambanova]' for SambaNova support\n"
        "pip install 'ai-gradio[hyperbolic]' for Hyperbolic support\n"
        "pip install 'ai-gradio[qwen]' for Qwen support\n"
        "pip install 'ai-gradio[fireworks]' for Fireworks support\n"
        "pip install 'ai-gradio[deepseek]' for DeepSeek support\n"
        "pip install 'ai-gradio[smolagents]' for SmolaAgents support\n"
        "pip install 'ai-gradio[jupyter]' for Jupyter support\n"
        "pip install 'ai-gradio[langchain]' for LangChain support\n"
        "pip install 'ai-gradio[all]' for all providers\n"
        "pip install 'ai-gradio[swarms]' for Swarms support"
    )

__all__ = ["registry"]
