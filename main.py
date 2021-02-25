from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:

    published_date = job.find('span', class_='sim-posted').span.text

    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')

        print('')

'''
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)


    # course_cards = soup.find_all('div', class_='card')
    # for course in course_cards:
    #     course_name = course.h5.text
    #     course_price = course.a.text.split()[-1]

    #     print(f'{course_name} costs {course_price}')

'''
