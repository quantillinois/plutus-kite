"""
A way to request the access token and api key from an endpoint.
"""
import requests
import json
import sys
from utils import read_env
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
## LOADING ENV VARS FROM .env
try:
    ENDPOINT = read_env("ENDPOINT")
except LookupError as err:
    raise LookupError("Did not find the following env variable") from err

def get_token_from_endpoint(ENDPOINT):
    """Fetches a access token from Kite using the endpoint

    Args:
        Endpoint (str): The endpoint to get the token from

    Raises:
       LookupError: In case the endpoint is not found

    Returns:
       str: The access token
       str: The api key
    """
    try:
        response = requests.get(ENDPOINT)
    except requests.exceptions.ConnectionError:
        raise LookupError("Could not connect to the endpoint") from None
    
    return response.json()["access_token"], response.json()["api_key"]


# if __name__ == "__main__":
#     print("This module is not meant to be run independently. \
#         Please run it through either hte main file or the streamer files, or as a test case.")
#     sys.exit(0)