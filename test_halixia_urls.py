
import csv
import requests

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:

f = open('resources/url-halixia-errors-14-10-23.csv', 'a')
f_whitelist = open('resources/url-whitelist.csv')

whitelist_urls = []
whitelist_reader = csv.reader(f_whitelist, delimiter=',')
for whitelist_url in whitelist_reader:
    whitelist_urls.append(whitelist_url)

writer = csv.writer(f)
links = []

def test_url(internal_name, link):
    if link and link not in links:
        links.append(link)
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

with open('resources/MA Database 220523.xlsx - CSV Import Format-v' + sys.argv[1] + '.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader, None)

    for row in reader:

        if count == 0:
            for i in range(0, len(row)):
                print(str(i) + ":" + header[i] + ":" + row[i])
        # print (count)
        internal_name = row[0]
        primary_link_1 = row[9]
        if "halixia" in primary_link_1:
            test_url(internal_name, primary_link_1)

        count = count + 1
        f.flush()

# close the file
f.close()
