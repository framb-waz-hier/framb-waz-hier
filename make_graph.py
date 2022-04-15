#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('files', nargs='+') # , type=argparse.FileType('r')

args = parser.parse_args()

if not args.files:
    parser.print_usage()
    sys.exit(EXIT_FAILURE)


for file in args.files:
    # print(file.readlines())

#     plt.rcParams["figure.figsize"] = [7.50, 3.50] # file.readlines()
#     plt.rcParams["figure.autolayout"] = True
#
#     headers = ["page_id","uri","type","date","count","id"]
#
#     df = pd.read_csv(file, names=headers)
#
#     df.set_index('Name').plot()
#
#     plt.show()

    x = []
    y = []
    date = ""
    with open(file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')

        # "page_id","uri","type","date","count","id"
        # "1","/index.php/la-page-qui-sert-a-rien/","page","2022-05-30","2","10"
        # "2","/","home","2022-05-30","1","0"
        # "3","/index.php/je-sais-pas-quoi-ecrire/","page","2022-05-30","1","8"
        # "4","/index.php/wordpress-la-loose/","page","2022-05-30","1","5"

        for row in plots:
            if len(row) != 6:
                break
            if row[0] == "page_id":
                print("row[0] is page_id")
                continue
            print("row[0] is '" + row[0] + "'")
            print(row[1])
            x.append(row[1])
            print(row[4])
            y.append(int(row[4]))
            print(row[3])
            date = row[3]

    plt.figure(figsize=(16, 12))
    plt.bar(x, y, color = 'g', width = 0.72, label = "")
    plt.xlabel('Pages')
    plt.ylabel('Nb of hits')
    plt.title('Number of hits per page on ' + date)
    plt.legend("by j-p peruvian")
    # plt.show()
    f = Path(file)
    plt.savefig(f.with_suffix('.png'))
