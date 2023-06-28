import requests
from bs4 import BeautifulSoup

# Function to extract data from a webpage
def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    questions = soup.find_all('h3')  # Find all h3 tags for questions

    for question in questions:
        question_text = question.text.strip()
        answer_texts = []

        # Find associated answers
        next_element = question.next_sibling
        while next_element and next_element.name not in ['h3', 'h4']:  # Stop at the next question
            if next_element.name == 'p' or next_element.name == 'li':
                answer_text = next_element.text.strip()
                answer_texts.append(answer_text)
            next_element = next_element.next_sibling

        data.append({'question': question_text, 'answers': answer_texts})

    return data

# Example usage
url = 'https://www.javatpoint.com/operating-system-interview-questions'  # Replace with the actual URL of the website
data = extract_data(url)
for item in data:
    print("Question:", item['question'])
    print("Answers:")
    for answer in item['answers']:
        print(answer)
    print("-----")
