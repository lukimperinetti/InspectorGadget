import requests
from bs4 import BeautifulSoup as bs  # create alias for BeautifulSoup

github_user = input('Input GitHub User: ')

while True:
    url = 'https://github.com/' + github_user
    r = requests.get(url)
    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')  # get content from URL html code
        profile_image = soup.find('img', {'class': 'avatar avatar-user width-full border color-bg-default'})[
            'src']  # ['src'] get the src attribute
        print('Success: '+profile_image)
        break
    else:
        print('User Not found or bad spelling -- Try again ? ')
        github_user = input('Input GitHub User: ')