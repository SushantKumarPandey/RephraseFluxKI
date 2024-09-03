import requests

def test_paraphrasing():
    # Send a POST request to the paraphrasing endpoint
    response = requests.post("http://localhost:8000/paraphrase/", json={"text": "Hello world!"})
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    # Check if the response contains 'paraphrased_text'
    result = response.json()
    assert "paraphrased_text" in result, "Response does not contain 'paraphrased_text'"
    
    # Print the result for manual inspection
    print("Paraphrased text:", result["paraphrased_text"])

# Run the test
if __name__ == "__main__":
    test_paraphrasing()

