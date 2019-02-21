import csv

def removeUrl(a):
    aux = ''
    for x in a.split(' '):
        if not('http' in x) and  x!='':
            aux+= ' '+x
    return aux

def readFile(fileName):
    obj={}
    types= []
    with open(fileName, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        data=[]
        for row in csv_reader:
            flag= True
            if line_count != 0:
                if not(row[0] in types):
                    obj[row[0]]=[]
                    types.append(row[0])
                    for x in row[1].split("'")[1].split('|||'):
                        for y in x.split("\\s"):
                            aux = removeUrl(y)
                            if len(aux)>0:
                                obj[row[0]].append(aux)
                else:
                    obj[row[0]].append(row[1].split('|||'))
            line_count += 1
        print(f'Processed {line_count} lines.')
    return obj
readFile('mbti_1.csv')  