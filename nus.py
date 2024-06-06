# nus.py
# Copyright (C) 2024 The New Shop Channel Team.
# Copyright 2024-2024 Fl0ppyB00k

import os 
import sys
import struct
import tickets
import requests
import ssl

http_session = requests.Session()
retry = requests.adapters.HTTPAdapter(max_retries=3)
http_session.mount('http://', retry)

def get_tik(base="http://nus.cdn.shop.wii.com/ccs/download"):
    titleid = tickets.tickets.index("TitleId")
    downloaded_tik = http_session.get(base, titleid, cetk) # type: ignore
    return downloaded_tik


def download_title(titleid, base="http://nus.cdn.shop.wii.com/ccs/download"):
    Title, ret = http_session.get(base, titleid, {contentid})
    if ret == 0 or ret < 0:
    

    return Title
