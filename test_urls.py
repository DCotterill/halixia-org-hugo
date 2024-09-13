
import csv
import requests
from datetime import date
import sys

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:
version = ""
if len(sys.argv) > 1:
    version = "-v" + sys.argv[1]

f = open('resources/url-errors-' + str(date.today().day) + '-' + str(date.today().month) + '-24.csv', 'a')
f_whitelist = open('resources/URL Check Outcomes.xlsx - Whitelist export' + version + '.csv')

whitelist_urls = []
whitelist_reader = csv.reader(f_whitelist, delimiter=',')
for whitelist_url in whitelist_reader:
    whitelist_urls.append(whitelist_url)

writer = csv.writer(f)
links = []

def is_whitelisted(link):
    for url in whitelist_urls:
        # print(url[0])
        if link.startswith(url[0]):
            return True
    return False

def test_url(internal_name, link):
    if link and link not in links:
        links.append(link)
        if is_whitelisted(link):
            print("Whitelist:" + link)
        else:
            # print("Testing:" + link)
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
                request = requests.get(link, timeout=10, headers = headers)
                if request.status_code != 200:
                    print("Error:" + link + ":" + request.status_code)
                    writer.writerow([link, request.status_code])
            except:
                print("Error:" + link )
                writer.writerow([internal_name, link, "Error"])

with open('resources/MA Database 230424.xlsx - Upload Prep' + version + '.csv'
        , newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader, None)

    for row in reader:

        if count == 0:
            for i in range(0, len(row)):
                print(str(i) + ":" + header[i] + ":" + row[i])
        category = row[1]
        # score = row[11]
        ddm_type = row[5]
        internal_name = row[8]
        # display_name = row[8]
        summary = row[10]
        description = row[11]
        # Content Type
        content_text = row[12]

        primary_link_1 = row[20]
        primary_link_2 = row[28]
        primary_link_3 = row[43]
        primary_link_4 = row[58]
        primary_link_5 = row[73]

        test_url(internal_name, primary_link_1)
        test_url(internal_name, primary_link_2)
        test_url(internal_name, primary_link_3)
        test_url(internal_name, primary_link_4)
        test_url(internal_name, primary_link_5)

        count = count + 1
        print(count)
        f.flush()

links = []

with open('resources/MA Database 230424.xlsx - CSV Import Format' + version + '.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader, None)
    print("Testing Halixia URLS....")
    for row in reader:

        if count == 0:
            for i in range(0, len(row)):
                print(str(i) + ":" + header[i] + ":" + row[i])
        print (count)
        internal_name = row[0]
        primary_link_1 = row[9]
        if "halixia" in primary_link_1:
            test_url(internal_name, primary_link_1)

        count = count + 1
        f.flush()

# close the file
f.close()
