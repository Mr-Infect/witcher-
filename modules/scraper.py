import requests
import re
from bs4 import BeautifulSoup
from time import sleep
from random import uniform
from . import utils, keywords, progress_bar

def scrape(url, custom_keywords=None, handler=None):
    session = requests.Session()
    user_agents = utils.get_user_agents()
    headers = {'User-Agent': utils.rotate_user_agent(user_agents)}

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        return
    except Exception as err:
        print(f"Error: {err}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Use handler if domain-specific logic is required
    if handler:
        handler.handle(soup)

    # Find critical information using regex
    critical_info = find_critical_info(soup, custom_keywords)

    # Display progress
    progress_bar.show_progress(url)
    
    # Display found details
    print(f"Critical Information Found for {url}:")
    for info in critical_info:
        print(info)

    # Sleep to avoid overloading the server
    sleep(uniform(1, 5))

def find_critical_info(soup, custom_keywords):
    keywords_list = custom_keywords if custom_keywords else keywords.DEFAULT_KEYWORDS
    critical_info = []

    for keyword in keywords_list:
        results = soup.find_all(string=re.compile(keyword, re.I))
        critical_info.extend(results)
    
    # Search for API keys and other patterns using regex
    api_keys = re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', soup.text)  # Example regex for API keys
    critical_info.extend(api_keys)

    return critical_info
