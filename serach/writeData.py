import csv #导入包

def writeData(data, name):
    with open(name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)
    print('write_csv success')