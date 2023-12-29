import requests

if __name__ == "__main__":
    res = requests.post('http://localhost:5000/query', json={"request_text": "Who are you?", "length":"20"})
    print(res.json())