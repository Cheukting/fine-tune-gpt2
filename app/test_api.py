import requests
import json
import sys
import time

def test_api(base_url="http://localhost:8000"):
    """
    Test the API endpoints
    """
    print("Testing API endpoints...")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
        print("Make sure the server is running.")
        sys.exit(1)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
    except Exception as e:
        print(f"Error testing health endpoint: {e}")
    
    # Test generate endpoint
    try:
        data = {
            "prompt": "A rectangle has a perimeter of 20 cm. If the length is 6 cm, what is the width?",
            "max_new_tokens": 200
        }
        
        print("Sending request to generate endpoint...")
        print(f"Prompt: {data['prompt']}")
        
        start_time = time.time()
        response = requests.post(
            f"{base_url}/generate", 
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        end_time = time.time()
        
        print(f"Generate endpoint: {response.status_code}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        
        if response.status_code == 200:
            result = response.json()
            print("\nGenerated text:")
            print("-" * 50)
            print(result["generated_text"])
            print("-" * 50)
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error testing generate endpoint: {e}")

if __name__ == "__main__":
    test_api()