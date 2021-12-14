#!/bin/env python3

import requests
import re
from sys import argv,stdin
import subprocess
from os import path

def doi2bib(doi, type="bibtex"):
    main_url = 'https://doi.org/'
    doi_pattern = r"10.\d{4,9}/[-._;()/:A-z0-9]+"
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
    if type == "bibtex":
        s.headers['Accept'] = 'application/x-bibtex'
    elif type == "json":
        s.headers['Accept'] = 'application/vnd.citationstyles.csl+json'

    res = s.get(main_url + doi)

    if res.ok:
        return res.text
    else:
        raise ValueError(main_url + doi + " returned " + str(res.status_code))

if __name__ == "__main__":
    if len(argv) > 1:
        doi = argv[1]
    else:
        try:
            doi = str(stdin.readlines()[0])
        except:
            'enter doi, url, or filepath'
    print(doi2bib(doi))
