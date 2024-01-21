#!/usr/bin/env python3
import argparse
import re
import sys

def scrapword(input_file, search_word, output_file):
    found = False
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if re.search(fr'\b{re.escape(search_word)}\b', line, re.IGNORECASE):
                outfile.write(line)
                found = True
    
    if not found:
        print(f'Sorry, "{search_word}" is not in the list.')

def main():
    parser = argparse.ArgumentParser(description='Scrapword: Extract lines containing a specified word from a list of subdomains.')
    parser.add_argument('input_file', help='Path to the input file containing subdomains')
    parser.add_argument('search_word', help='Word to search for in subdomains')
    parser.add_argument('-o', '--output_file', help='Path to the output file', default='output.txt')

    args = parser.parse_args()
    scrapword(args.input_file, args.search_word, args.output_file)

if __name__ == "__main__":
    main()

