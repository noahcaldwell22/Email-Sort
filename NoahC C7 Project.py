#! /usr/bin/env python3

import csv

FILENAME = 'prospects.csv'
CLEANFILE = 'prospects_clean.csv'

def display_menu():
    print('Welcome to the Email List Cleaner')
    print(f'\nSource List:  {FILENAME} \nCleaned List: {CLEANFILE}')

def read_names():

    prospects = []
    with open(FILENAME,'r',newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            prospects.append(row)
        return prospects

def format_names(prospects):
    with open(CLEANFILE,'w', newline = '') as outfile:
        writer = csv.writer(outfile)

        formatted_names = []
        for row in prospects:
            first_name = row[0].strip()
            last_name = row[1].strip()
            email = row[2].title()

            formatted_names.append([first_name.title(), last_name.title(), email.lower()])
        writer.writerows(formatted_names)
        

def main():
    display_menu()


if __name__ == '__main__':
    main()

    prospects = read_names()
    format_names(prospects)

    print ('\nCongrats! Your list has been cleaned!')

 