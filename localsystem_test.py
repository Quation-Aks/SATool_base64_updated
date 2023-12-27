# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:54:18 2023

@author: Quation
"""



import requests
import json
import base64

# Replace these with the actual URLs of your API endpoints
data_url = "http://52.87.149.214/api/data/CTA_Meghana_Foods.csv"
images_url = "http://52.87.149.214/api/images?download=true"
list_files_url = "http://52.87.149.214/api/list_files"

# # Example payload for the /api/images endpoint
# images_payload = {
#     "image_names": ["NOS_FI", "NOS_NAI_Stdev"]
# }

def test_data_endpoint():
    # Make a GET request to the /api/data endpoint
    response = requests.get(data_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data (replace this with your processing logic)
        data = response.json()
        print("Data from /api/data endpoint:", data)
    else:
        print(f"Error: {response.status_code}\n{response.json()}")

def test_images_endpoint():
    try:
        # Make a GET request to the /api/images endpoint
        response = requests.get(images_url)
        
        # Raise an exception for non-200 status codes
        response.raise_for_status()

        print("Response with download (HTTP 200):")
        print(json.dumps(response.json(), indent=2))

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def test_list_files_endpoint():
    # Make a GET request to the /api/list_files endpoint
    response = requests.get(list_files_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data (replace this with your processing logic)
        files = response.json()
        print("Files from /api/list_files endpoint:", files)
    else:
        print(f"Error: {response.status_code}\n{response.json()}")

if __name__ == "__main__":
    # Run the test functions
    test_data_endpoint()
    test_images_endpoint()
    test_list_files_endpoint()
