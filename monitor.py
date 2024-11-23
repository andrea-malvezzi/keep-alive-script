import requests
import datetime

def ping_website(url:str, page:str) -> bool:
    """
    Ping the route specified via parameters and print the status code returned from the request.\n
    Returns True if the website responded with a Status Code of 200, and False in every other case.
    """
    try:
        response = requests.get(url + '/' + page)
        if response.status_code == 200:
            print(f"✅ {datetime.datetime.now()}: {url} is up! Status code: {response.status_code}")
            return True
        elif response.status_code == 403:
            print(f"❌ {datetime.datetime.now()}: Access to {url} is forbidden (Status Code {response.status_code}).")
            return False
        else:
            print(f"❌ {datetime.datetime.now()}: Failed to ping {url}. Status Code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error pinging {url}/{page}: {e}")
    
if __name__ == "__main__":
    ping_website('https://www.thegaminglair.com', 'status')