import sys
from scrapers import ciper


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def run_scraper(name):
    if name == 'ciper':
        print('hola')
        return ciper()


if __name__ == '__main__':
    print(sys.argv[1])
    run_scraper(sys.argv[1])
