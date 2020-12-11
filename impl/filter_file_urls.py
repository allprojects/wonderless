import pandas as pd
import csv


# change the format of the file to csv
def txt_to_csv(txt_file, csv_file):
    df = pd.read_fwf(txt_file)
    df.to_csv(csv_file)


# remove projects developed by the Serverless framework community
# remove projects that their config file is in a template, example, demo, or test directory
def filter_urls(file_urls, filtered_file_urls):
    wtr = csv.writer(open(filtered_file_urls, 'w'), lineterminator='\n')
    wtr.writerow(['File_URL'])

    remove = ['/templates/', '/template/', '/examples/', '/example/', '/demos/', '/demo/',
              '/test/', '/tests/', '/github.com/serverless/', '/github.com/serverless-components/']

    with open(file_urls, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            if any(c in row[1].lower() for c in remove):
                continue
            else:
                wtr.writerow([row[1]])

# ----------------------------- MAIN --------------------------------------


txt_to_csv('result-2020-07-29.txt', 'file_url.csv')
filter_urls('file_url.csv', 'file_urls.csv')
