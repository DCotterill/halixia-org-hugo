
import csv

content_pages = {}
count = 0
# with open('resources/Dummy Data_final_310123 - with full content samples.xlsx - Full Content Samples.csv'
#         , newline='') as csvfile:
with open('resources/MA Database 220523.xlsx - topics.csv'
        , newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    topics_h = set()
    topics_w = set()
    topics_c = set()
    topics_l = set()
    for row in reader:
        topic = row[7]
        pillar = row[0]
        # print(pillar)
        if pillar == "Health":
            for t in topic.split(","):
                topics_h.add(t)
        if pillar == "Wealth":
            for t in topic.split(","):
                topics_w.add(t)
        if pillar == "Community":
            for t in topic.split(","):
                topics_c.add(t)
        if pillar == "Learning":
            for t in topic.split(","):
                topics_l.add(t)

    print("--- HEALTH")
    for t in sorted(topics_h):
        print(t)
    print("")
    print("--- WEALTH")
    for t in sorted(topics_w):
        print(t)
    print("")
    print("--- COMMUNITY")
    for t in sorted(topics_c):
        print(t)
    print("")
    print("--- LEARNING")
    for t in sorted(topics_l):
        print(t)
    print("")

