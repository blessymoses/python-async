"""
   Download all sites - using threads
"""
import concurrent.futures
import threading
import time

import requests
from requests.sessions import session

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
