import xlwings as xw
import pandas as pd
df = pd.DataFrame([[1, 2],[3, 4]],
                  columns = ['c1,c2'],
                  index = ['r1', 'r2'])
wb = xw.book()
sheet = wb.sheets['sheet1']

sheet.range('A1').value = df
sheet.range('A1').(pd.DataFrame, expand = 'table').valueoptions