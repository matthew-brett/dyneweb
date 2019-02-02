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


def check_bib(bibfile):
    with open(bibfile, 'rt') as bibfile:
        bp = BibTexParser(bibfile.read())
        entries = bp.get_entry_list()
        for entry in entries:
            keywords = entry['keyword'] if 'keyword' in entry else ''
            id = entry['ID']
            keywords = split_keywords(keywords)
            if len(TYPE_CLASSIFIERS.intersection(keywords)) != 1:
                raise RuntimeError(
                    'type classifiction seems wrong {}, {}'.format(
                        id, keywords))
            if ARTICLE_TYPES.intersection(keywords):
                if len(TOPIC_CLASSIFIERS.intersection(keywords)) != 1:
                    raise RuntimeError(
                        'topic classifiction seems wrong {}, {}'.format(
                            id, keywords))


def main():
    parser = argparse.ArgumentParser(description='Process bib file.')
    parser.add_argument('bibfile', help='bib file')
    args = parser.parse_args()
    check_bib(args.bibfile)


if __name__ == '__main__':
    sys.exit(main())
