import requests
from bs4 import BeautifulSoup
import pandas as pd

def extractData():
    # response = requests.get(url)
    with open('response.html', 'r') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    data = []
    questions = soup.find_all('h3', class_='h3')

    for index, question in enumerate(questions):
        ques_text = question.text.strip()
        answer_texts = []

        next_element = question.next_sibling
        while next_element and not (next_element.name == 'h3' and index > 0):
            if next_element.name == 'p':
                answer_texts.append(next_element.text.strip())
            elif next_element.name in ['ul', 'ol']:
                bullet_points = next_element.find_all('li')
                answer_text = ''
                for bullet_point in bullet_points:
                    bullet_text = bullet_point.text.strip()
                    answer_text += f"- {bullet_text}\n"
                answer_texts.append(answer_text.strip())
            next_element = next_element.next_sibling

        data.append({'questions': ques_text, 'answers': answer_texts})

    return data

# def extractData():
#     # response = requests.get(url)
#     with open('response.html', 'r') as file:
#         html = file.read()
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(soup)
    

#     data = []
#     question = soup.find_all('h3',class_='h3')

#     for ques in question:
#         ques_text = ques.text.strip()
#         answer_texts = []

#         next_element = ques.next_sibling
#         while next_element and next_element.name != ['h3','hr']:
#             if next_element.name == 'p':
#                 if next_element.find_next('ul', class_='points'):
#                     bullet_points = next_element.find_next('ul', class_='points').find_all('li')
#                     answer_text = next_element.text.strip()
#                     for bullet_point in bullet_points:
#                         bullet_text = bullet_point.text.strip()
#                         answer_text += f"\n- {bullet_text}"
#                     answer_texts.append(answer_text)
#                 elif next_element.find_next('ol', class_='points'):
#                     bullet_points = next_element.find_next('ol', class_='points').find_all('li')
#                     answer_text = next_element.text.strip()
#                     for bullet_point in bullet_points:
#                         bullet_text = bullet_point.text.strip()
#                         answer_text += f"\n- {bullet_text}"
#                     answer_texts.append(answer_text)
#                 else:
#                     answer_text = next_element.text.strip()
#                     answer_texts.append(answer_text)
#             next_element = next_element.next_sibling
#         data.append({'questions': ques_text, 'answers': answer_texts})

#     return data

url = "https://www.javatpoint.com/operating-system-interview-questions"
data = extractData()

df = pd.DataFrame(data)  # Convert the list of dictionaries to a DataFrame
df.to_csv('dataset.csv', index=False)  # Save the DataFrame to a CSV file
print(df)
print("Data saved to data.csv")
