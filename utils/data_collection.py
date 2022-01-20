import os
import json
import requests # for accessing apis and subsequently downloading data 
from tqdm import tqdm
from _apikey import apikey

def download(url: str, fname: str): 
    """
    util function to download file from given url to disk, and display progress bar  

    Args:
        url (str): url to download  
        fname (str): file path to save to 
    """
    response = requests.get(url,stream=True) # stream allows chunking as large file 
    total = int(response.headers.get('content-length',0))
    with open(fname,'wb') as file, tqdm(desc=fname, 
                                        total=total, 
                                        unit='iB',
                                        unit_scale=True, 
                                        unit_divisor=1024,
                                        ) as bar: 
        for data in response.iter_content(chunk_size=1024): 
            size = file.write(data) 
            bar.update(size)

base_url = 'https://use-land-property-data.service.gov.uk/api/v1/'

headers = {'Accept':'application/json', 
           'Authorization':apikey}

available_datasets = [
    {
    "name": "ccod",
    "title": "UK companies that own property in England and Wales"
    },
    {
    "name": "ocod",
    "title": "Overseas companies that own property in England and Wales"
    },
    {
    "name": "nps",
    "title": "National Polygon Service"
    },
    {
    "name": "nps_sample",
    "title": "National Polygon Service Sample"
    }
]

if not os.path.exists(os.path.join(os.getcwd(),'data')):
    os.mkdir(os.path.join(os.getcwd(),'data')) 

for dataset in ['ccod','ocod']:
    if not os.path.exists(os.path.join(os.getcwd(),'data',f'{dataset}_data.csv')):
        print('Working on producing CCOD dataset...')
        # first get filename for most recent dataset 
        get_timestamped_fname = requests.get(url=base_url+f'datasets/{dataset}',headers=headers)
        # print(get_timestamp_ccod_data.status_code)
        # print(json.dumps(ccod_data_url.json(),indent=4))
        if get_timestamped_fname.status_code == 200:
            print('Obtained file name for most recent dataset')
            data_file_name = get_timestamped_fname.json()['result']['resources'][1]['file_name']
            # now get url to download full dataset
            data_url = requests.get(url=base_url+f'datasets/{dataset}/{data_file_name}',headers=headers)
            # print(json.dumps(ccod_data_url.json(),indent=4))
            print(f'Obtained download URL for {dataset.upper()} dataset')
            print('Downloading now...')
            download(data_url.json()['result']['download_url'],f'./data/{dataset}_data.csv')        
        else:
            raise Exception(f'Failed to access initial API endpoint for {dataset.upper()} dataset - check connection and API credentials')

     
    
    
    


