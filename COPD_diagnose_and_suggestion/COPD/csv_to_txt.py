##coding=utf8
import csv
def csv_to_text(csvname, txtname, iswithheader = 0):
    ''' 默认有表头'''
    with open(csvname, 'rb') as f:
        reader = csv.reader(f, delimiter='\t', quotechar='|') ## 分隔符
        rowlist = list()
        with open(txtname, 'wb') as txt:
            for row in reader:
                if iswithheader:
                    iswithheader = 0
                else:
                    rowlist.append(row[0])
            txt.write('\n'.join(rowlist))
csv_to_text('copd_1000.csv', 'copd_1000.txt', 0)