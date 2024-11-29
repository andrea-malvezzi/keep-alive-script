import requests
import datetime
import logging
import os

# Create logs dir if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Set up logging
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    # timestamp, severity (info, warning, error) and message
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ping_website(url:str, page:str) -> bool:#
    """
    Ping the route specified via parameters with multiple retry attempts and timeout.
    
    Args:
        url (str): Base URL to ping
        page (str): Specific page/endpoint to check
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        bool: True if website is accessible, False otherwise
    """
    try:
        response = requests.get(f"{url}/{page}")
        if response.status_code == 200:
            logging.info(f"✅ {datetime.datetime.now()}: {url} is up! Status code: {response.status_code}")
            return True
        elif response.status_code == 403:
            logging.warning(f"❌ {datetime.datetime.now()}: Access to {url} is forbidden (Status Code {response.status_code}).")
            return False
        else:
            logging.error(f"❌ {datetime.datetime.now()}: Failed to ping {url}. Status Code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error pinging {url}/{page}: {e}")
    
def main():
    websites = [
        # Add more if needed
        { 'url' : 'https://www.thegaminglair.com', 'page' : 'status' },
    ]

    logging.info(f"📡 Logging started...")
    for site in websites:
        ping_website(site['url'], site['page'])

if __name__ == "__main__":
    main()