#!/bin/env python3

import requests
import re
from sys import argv,stdin
import subprocess
from os import path

main_url = 'https://doi.org/'
doi_pattern = r"10.\d{4,9}/[-._;()/:A-z0-9]+"
s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'

if len(argv) > 1:
    doi = argv[1]
else:
    try:
        doi = str(stdin.readlines()[0])
    except:
        'enter doi, url, or filepath'

def most_frequent(l):
    return max(set(l), key = l.count)

def get_url_content(url):
    content = s.get(url).text
    return check_content(content)

def get_pdf_content(filepath):
    filepath = path.realpath(filepath).replace(' ','\\ ')
    out_file = '/tmp/doi_content'
    content = subprocess.getoutput('pdftotext ' + str(filepath) + ' ' + out_file + ' && cat ' + out_file)
    return check_content(content)

def check_content(content):
    global doi_pattern
    doi_list = re.findall(doi_pattern, content)
    try:
        return most_frequent(doi_list)
    except:
        print('no doi found')
        return ''

def check_url(url, doi_pattern):
    return re.search(doi_pattern, url).group()


doi = doi.replace('https://doi.org/','')

if path.isfile(doi):
    doi = get_pdf_content(doi)
else:
    try:
        # try to match doi in url / doi directly
        doi = check_url(doi, doi_pattern)
    except:
        # get website content and try to match doi
        doi = get_url_content(doi)

print(doi)
