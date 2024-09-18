import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# define the BTS URL and download directory
base_url = "https://www.bts.gov/browse-statistical-products-and-data/bts-publications/data-bank-28ds-t-100-domestic-segment-data"
download_dir = "./downloads"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# define the target file URL (this is the file you want to stop at)
target_url = "https://www.bts.gov/sites/bts.dot.gov/files/docs/airline-data/domestic-segments/DD.DB28DS.WAC.201307.201406.REL01.04SEP2014.zip"

# function to download and unzip a ZIP file
def download_and_unzip(zip_url, download_dir):
    try:
        file_name = zip_url.split("/")[-1]
        zip_file_path = os.path.join(download_dir, file_name)
        
        # download the file
        print(f"Downloading {file_name} from {zip_url}")
        response = requests.get(zip_url)
        if response.status_code == 200:
            with open(zip_file_path, 'wb') as zip_file:
                zip_file.write(response.content)
            print(f"Downloaded {file_name}")

            # unzip the file
            with ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)
            print(f"Unzipped {file_name}")
            
            # remove the ZIP file after extraction
            os.remove(zip_file_path)
        else:
            print(f"Failed to download {zip_url} (Status code: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {zip_url}: {e}")

# function to scrape the webpage to find all download links
def scrape_bts_page(base_url, download_dir, target_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all the anchor tags that contain the download links
    links = soup.find_all('a', href=True)
    
    # filter out links that are ZIP files
    zip_links = [link['href'] for link in links if link['href'].endswith('.zip')]

    # loop through each ZIP link and download files until the target file is reached
    for zip_link in zip_links:
        # some links might be relative, so we need to construct the full URL
        if zip_link.startswith('/'):
            zip_link = f"https://www.bts.gov{zip_link}"

        # stop downloading once the target URL is reached
        if zip_link == target_url:
            print(f"Stopping download. Reached the target file: {target_url}")
            break

        # download and unzip files before the target
        download_and_unzip(zip_link, download_dir)

# call the function to start the download process
scrape_bts_page(base_url, download_dir, target_url)
