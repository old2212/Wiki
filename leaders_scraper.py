# 22 lines
import re
import json
import requests
from bs4 import BeautifulSoup

def get_leaders():
    #define my URLs
    root_url = "https://country-leaders.herokuapp.com"
    leaders_url = root_url + "/leaders"
    countries_url = root_url + "/countries"
    cookie_url = root_url + "/cookie"
    
    #query cookie
    req_cookie = requests.get(cookie_url)
    cookie = req_cookie.cookies

    #query countries
    req_country = requests.get(countries_url, cookies=cookie)
    countries = req_country.json()
    
    session = requests.Session()

    #create my dictionnary
    leaders_per_country = {}
    
    #loop to add to my dictionnary
    for country_code in countries :
        leaders_req = requests.get(leaders_url, cookies=cookie, params={"country":country_code})

        if leaders_req.status_code == 403:
            cookie = requests.get( cookie_url).cookies
            leaders_req = requests.get(leaders_url, cookies=cookie, params={"country":country_code})

        leaders = leaders_req.json()
        #leaders_per_country[country_code] = leader_req.json()
            
        #get first paragraph from the wikipedia_url in the leader info
        #print(leaders)
        for leader in leaders:
            leader["first_paragraph"] = get_first_paragraph(leader["wikipedia_url"], session)
        
        leaders_per_country[country_code] = leaders
        
    return leaders_per_country

def hashable_cache(f):
    def inner(url, session):
        if url not in cache:
            cache[url] = f(url, session)
        return cache[url]
    return inner

@hashable_cache
def get_first_paragraph(wikipedia_url, session):
    #print(wikipedia_url) # keep this for the rest of the notebook
    content = session.get(wikipedia_url).content
    soup = BeautifulSoup(content, "html.parser")

    first_paragraph = " "
    for para in soup.find_all("p"): 
        if para.find("b"):
            pattern = r" \([^()]*\)"
            repl = ""
            first_paragraph += re.sub(pattern, repl, para.get_text())
            break
    
    return first_paragraph

def save(file_name) :
    with open('leaders.json', 'w') as f:
        json.dump(leaders_per_country, f)
    print('Json file saved')

#Here is everything I call 
if __name__ == "__main__":
    cache={}
    leaders_per_country = get_leaders()
    save(leaders_per_country)
