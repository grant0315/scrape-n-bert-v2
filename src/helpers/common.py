import requests
from urllib.parse import urlparse
import os.path as osp

def check_if_url_is_accessible(url):
    try:
      statusCode = str(requests.head(url))
      print("\nURL return status code: " + statusCode)
      print("--- Website was reachable ---\n")
      return True
    
    except requests.exceptions.MissingSchema as e:
      print(type(e), type(e).__qualname__)
      print("--- Website was NOT reachable ---")
      return False

def check_if_file_exists(file_path):
    return osp.isfile(file_path)

def check_if_directory_exists(directory):
    return osp.isdir(directory)

def remove_scheme_from_url(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1).replace("/", "")