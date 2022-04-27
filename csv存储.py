import csv
def write_to_file(content):
    col = ["热榜排名", "热榜链接", "热榜标题", "热榜内容", "热榜热度"]
    with open('.\\re知乎热榜.csv', 'w+',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for loop in range(51):
            if loop == 0:
               writer.writerow(col)
            else:
                writer.writerow(content[loop-1])
