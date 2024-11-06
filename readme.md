# Handwriting Extractor

A simple Python script that uses Ollama's vision model to extract handwritten text from images.
Used to test [LLAMA3.2 Vision](https://ollama.com/blog/llama3.2-vision)

## Prerequisites

- Python 3.6+
- Ollama server running (version 0.4.0+)
- llama3.2-vision model pulled in Ollama : `ollama run llama3.2-vision`

## Installation

1. Clone this repository:

```bash
git clone [repository-url]
cd handwriting-extractor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Ollama server URL (optional, defaults to localhost):

```bash
OLLAMA_URL=http://localhost:11434
```

## Usage

Run the script with an image path:

```bash
python extract_handwriting.py path/to/your/image.jpg
```

The script will output only the extracted text from the handwriting in the image.

## Error Handling

- If the image cannot be found, the script will display a usage message
- If Ollama server is not accessible, it will display a connection error
- If the model fails to process the image, it will display the error message

## License

This project follows the MIT License conventions. Feel free to use, modify, and distribute as per MIT License terms.
