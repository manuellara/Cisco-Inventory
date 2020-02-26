import os
import pandas as pd

def openFile( x , sheetName, workBook ):
    counter = 0
    innerArr = []
    temp = []

    with open ( x , encoding="utf8", errors='ignore' ) as target:
        for line in target:

            if( line.rstrip() != '' ):
                temp.append(line)

                counter += 1

            if counter == 25:
                innerArr.append(temp)
                temp = []
                counter = 0
            
    df = pd.DataFrame(innerArr)
    df.to_excel(workBook, sheet_name = sheetName, index = False)

# main
writer = pd.ExcelWriter('inventory.xlsx', engine='xlsxwriter')

for filename in os.listdir( os.getcwd() ):
    if filename == "iusd.py" or filename == "inventory.xlsx" or filename == ".DS_Store":
        continue

    openFile( filename, os.path.splitext(filename)[0], writer )

writer.save()