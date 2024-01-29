# Semi Auto Translator

**Semi Auto Translator** is a Visual Studio Code extension. This software allows users to translate bilingual texts semi-automatically in different languages, using well-known dictionaries such as Trung-Viet. This software supports many languages such as English, Vietnamese, Chinese, French, etc. The initial purpose of this software is to translate Chinese to Vietnamese for Vietnamese people who want to read Chinese stories. This software also has features such as pronunciation, spell check, and code formatting.

# Refers
## VS Code Extension

> https://code.visualstudio.com/api



## Large Language Model

> https://github.com/abetlen/llama-cpp-python
> https://llama-cpp-python.readthedocs.io/
> https://github.com/abetlen/llama-cpp-python/tree/main/examples

# Setup
## Initial
### vs-code

```console
codex-demo$ npm install -g yo generator-code
```

### llama-cpp

1. Create/Active virtual environment

```console
llm-demo$ python -m venv venv
llm-demo$ .\venv\Scripts\activate
```

2. Run docker 

```console
llm-demo$ docker pull ghcr.io/abetlen/llama-cpp-python:latest
llm-demo$ docker run --rm -it -p 8000:8000 -v C:/Users/cuong/workspace/ai/models:/models -e MODEL=/models/mistral.7b.openhermes-2.5.gguf_v2.q4_k_m.gguf ghcr.io/abetlen/llama-cpp-python:latest
```