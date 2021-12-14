import tabula as tb
import pandas as pd

file1 = "padrao-tiss_componente-organizacional_202111.pdf"

table = tb.read_pdf(file1, output_format="dataframe", multiple_tables=False, pages="114") 
data = pd.DataFrame(data=table[0])

print(data)
print(type(data))
print(data.info())

newd = data.dropna()
print(newd)



