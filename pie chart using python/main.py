import pandas as pd
from matplotlib import pyplot as plt

data = {'Categories': ['Subject A',' SubjectB','Subject C','Subject D',],
        'Sizes':[15,30,45,10]}

df=pd.DataFrame(data)
df.set_index('Categories',inplace=True)

ax= df.plot.pie(y='Sizes',autopct='%1.1f%%', startangle=140,legend=False)
ax.set_ylabel('')
plt.title('Pie chart')
plt.show()
