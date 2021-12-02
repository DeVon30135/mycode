import requests

url = "http://10.1.103.80:2224/answer"
def post():
    correct_data = {"answer": "blue paint"}
    incorrect_data = {"answer": "yellow paint"}

    correct = requests.post(url, json=correct_data).text
    incorrect = requests.post(url, json=incorrect_data).text

    print(f"Correct Post: {correct}")
    print(f"Incorrect Post: {incorrect}")

if __name__ == "__main__":
    post()
