#!/usr/bin/python3

#Attempts to locate links to free ebooks for a specified title, if available

import requests
import argparse
import pprint
import webbrowser

__author__="Kevin Pluas"
__version__="0.1.0"
__license__="MIT"

MAX_RESULTS = 3 # Amount of books to return from the search

def main(args):
    print("Searching for free eBook links for: " + args.title)
    title_search = args.title
    Base_URL = "https://www.googleapis.com/books/v1/volumes?q="
    response = requests.get(Base_URL + title_search + 
                            "&filer=full&filter=free-ebooks&projection=lite")

    if 'items' not in response.json():
        print("Sorry, no eBook available for that title")
        return

    results = response.json()['items']
    
    top_results = []
    results = response.json()['items']
    
    for i in range(len(results)):
        top_results.append(results[i])
        pprint.pp(str(i) + ': ' + top_results[i]['volumeInfo']['title'] + ' ' 
                  +top_results[i]['volumeInfo']['canonicalVolumeLink'])
    
    while True:
        try:
            num = int(input("Please select a link to open (Enter a number): "))
            if num in range(len(results)):
                break
            else:
                print("Your selection out of range. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
    
    try:
        webbrowser.open(top_results[num]['volumeInfo']['canonicalVolumeLink'])
    except webbrowser.Error:
        print("Error: Could not open up browser. Exitting...")
        return
    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("title", help="Title of the book to search for")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)