import argparse
import csv
from os import listdir

def capture():
    parser = argparse.ArgumentParser(description="Script functionality description")
    parser.add_argument("name", help = "It is the name that you want to consult")
    argument = parser.parse_args()
    return argument


def standarize_name(argument):
    name = argument.name
    name = name.upper()
    return name


def search_name(name,count):
    data = listdir("Data")
    for file in data:
        with open("Data/" + file) as actual_file:
            csv_reader = csv.reader(actual_file, delimiter=",")
            for row in csv_reader:
                if row[0] == name or row[1] == name:
                    count = count+1
    return count

if __name__ == "__main__":
    count_year = 0
    argument = capture()
    name = standarize_name(argument)
    count_year = search_name(name,count_year)
    print("The name {} is among the most popular names in {} years".format(name,count_year))