import sys
from ollama import Client, ResponseError
import os
from dotenv import load_dotenv

load_dotenv()


def extract_handwriting(image_path, stream=False):
    client = Client(host=os.getenv("OLLAMA_URL", "http://localhost:11434"))
    try:
        response = client.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "user",
                    "content": "Extract ONLY the handwritten text from this image. Provide ONLY the text, no descriptions or explanations.",
                    "images": [image_path],
                }
            ],
        )
        return response["message"]["content"].strip()
    except ResponseError as e:
        print("Error:", e.error)
        return None
    except Exception as e:
        print("Unexpected error:", str(e))
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_handwriting.py <image_path>")
        sys.exit(1)

    result = extract_handwriting(sys.argv[1])
    if result:
        print(result)


if __name__ == "__main__":
    main()
