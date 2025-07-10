# Openai API Wrapper

This repository encapsulates the Python package of the OpenAI API, which supports text and image chat input formats, allowing you to quickly build multi-role, image-supported AI dialogue applications.

---

## Installation

### 1. Clone this repository
```bash
git clone https://github.com/TKUwengkunduo/openai_api_wrapper.git
```

### 2. Install `openai_client`
```bash
cd openai_api_wrapper
pip install -e .
```

### 3. Setting environment variables
```bash
export OPENAI_API_KEY=<your_openai_api_key>
```

---

## Execution example

### 1. hello example
#### most basic examples
```bash
python3 ./example/hello_example.py
```

### 2. setting example
#### Set temperature and model examples
```bash
python3 ./example/stream_example.py
```

### 3. stream example
#### Live Streaming Example
```bash
python3 ./example/setting_example.py
```

### 4. image example
#### Examples containing images
```bash
python3 ./example/image_example.py
```