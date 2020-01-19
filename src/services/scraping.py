import requests
from bs4 import BeautifulSoup

from config.settings import URL_PACK

page = requests.get(URL_PACK)
soup = BeautifulSoup(page.content, 'html.parser')

def get_tools():
    containers = soup.find_all('container-lg')
    
    # find the container that wraps the tool cards
    tool_cards = next( (c for c in containers if container.name=='div' and container.find('dl') is not None), None)
        
