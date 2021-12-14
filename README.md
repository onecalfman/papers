# papers
A simple manager for scientific ressources and citations

This scripts creates a list of scientific ressources from dois, webpages or pdfs.
If a website or pdf is given the script tries to find a doi by matching with regex.
If no doi can be obtained the process in canceled.

Otherwise the bibtex file from doi.org will be obtained and added.
The bibliography is stored as a json and bib file.
It will also be attempted to obtain a pdf version of the given article from sci-hub.
This behaviour can be disables in the config file with the "localpdf" option

## Adding paper

    papers -a https://www.science.org/doi/10.1126/science.352.6285.508
    or
    papers -a 10.1126/science.352.6285.508

## Editing

    papers -e

A copy for editing will be made. On write and close the changes to the bib file will
be shown and writte to the main file on confirmation.

## Tags and Notes

I extended the bibtex format a bit to allow tags an notes. Those proved helpful
while selecting papers.

    # add the tags "math" and "dgl" to the paper with id "Bohannon_2016"
    papers -t math dgl -i Bohannon_2016

    # add the tags "math" and "dgl" to the paper selected interactivly
    papers -t math dgl

    # add the note "dark side of the moon" to the interactivly selected paper
    papers -n dark side of the moon

## Selection

    # use dmenu to select a paper and open the pdf file
    papers -d open

    # use fzf to select a paper and open the pdf file
    papers -z open

Options are:

- open
- url
- doi
- id

## Installation

As this project is work in progress no real install method exists.
The main file "papers" and the other two .py files need to be places in the same directory.
