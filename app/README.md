# Text Generation API

This is a FastAPI server that provides endpoints to chat with a text generation model.

## Installation

1. Make sure you have Python 3.13+ installed
2. Install the required dependencies:

```bash
# From the project root directory
pip install -e .
# Or if using uv
uv pip install -e .
```

## Usage

### Starting the server

From the project root directory:

```bash
cd app
python run.py
```

This will start the server at http://0.0.0.0:8000

### API Endpoints

#### Root endpoint

```
GET /
```

Returns a welcome message.

#### Health check

```
GET /health
```

Checks if the API and model are working properly.

#### Generate text

```
POST /generate
```

Request body:

```json
{
  "prompt": "A rectangle has a perimeter of 20 cm. If the length is 6 cm, what is the width?",
  "max_new_tokens": 200
}
```

Response:

```json
{
  "generated_text": "The generated text response from the model..."
}
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: http://0.0.0.0:8000/docs
- ReDoc: http://0.0.0.0:8000/redoc