#!/usr/bin/env python
""" Check bibliography for classification errors """
from __future__ import print_function

import sys
import argparse
from bibtexparser.bparser import BibTexParser


ARTICLE_TYPES = set(('abstract', 'article'))
TYPE_CLASSIFIERS = ARTICLE_TYPES.union(('software', 'online'))
TOPIC_CLASSIFIERS = set(('movethink', 'methods', 'computing', 'others'))

def split_keywords(keywords):
    words = [s.strip() for s in keywords.split(';')]
    end_word = words[-1]
    words = words[:-1]
    if end_word != '': # No final semicolon
        words += [s.strip() for s in keywords.split(',')]
    return words


def main():
    parser = argparse.ArgumentParser(description='Process bib file.')
    parser.add_argument('bibfile', help='bib file')
    args = parser.parse_args()
    with open(args.bibfile, 'rt') as bibfile:
        bp = BibTexParser(bibfile.read())
        entries = bp.get_entry_list()
        for entry in entries:
            keywords = entry['keyword']
            id = entry['ID']
            keywords = split_keywords(keywords)
            if len(TYPE_CLASSIFIERS.intersection(keywords)) != 1:
                print('type classifiction seems wrong', id, keywords)
                return 1
            if ARTICLE_TYPES.intersection(keywords):
                if len(TOPIC_CLASSIFIERS.intersection(keywords)) != 1:
                    print('topic classifiction seems wrong', id, keywords)
                    return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
