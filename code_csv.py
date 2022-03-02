import csv  

header = ['comment', 'polarity']

comment = 'haha'
polarity = 3
list = []
data1 = [comment,polarity]
data2 = ['comment','1']
data3 = ['comment','3']

list.append(data1)
list.append(data2)
list.append(data3)

with open('comment.csv', 'w',newline='', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(list)):
        print(i)
        writer.writerow(list[i])



print(list[1])