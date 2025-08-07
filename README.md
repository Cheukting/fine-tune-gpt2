# Text Generation Model with FastAPI Server

This project contains a fine-tuned text generation model and a FastAPI server to interact with it.

## Project Structure

- `trained_model/`: Contains the fine-tuned text generation model (need to be created with `fine_tune_model.ipynb`)
- `model.py`: Script to directly use the model for text generation
- `app/`: FastAPI server for interacting with the model through API endpoints
  - `main.py`: FastAPI application with API endpoints
  - `run.py`: Script to run the FastAPI server
  - `test_api.py`: Script to test the API endpoints
  - `README.md`: Documentation for the API server

## Installation

1. Make sure you have Python 3.13+ installed
2. Install the required dependencies:

Using pip with pyproject.toml:
```bash
# From the project root directory
pip install -e .
# Or if using uv
uv pip install -e .
```

Alternatively, using requirements.txt:
```bash
pip install -r requirements.txt
# Or if using uv
uv pip install -r requirements.txt
```

## Usage

### Direct Model Usage

You can use the model directly with the `model.py` script:

```bash
python model.py
```

### API Server

To start the FastAPI server:

```bash
cd app
python run.py
```

This will start the server at http://0.0.0.0:8000

For more details on the API endpoints and usage, see the [API documentation](app/README.md).

### Testing the API

After starting the server, you can test the API endpoints:

```bash
cd app
python test_api.py
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: http://0.0.0.0:8000/docs
- ReDoc: http://0.0.0.0:8000/redoc