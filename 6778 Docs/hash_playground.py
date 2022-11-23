import pandas as pd
import matplotlib.pyplot as plt


data = dict([('a', [11, 10]), ('b', [10, 11]), ('c', [7, 6]), ('d', [5, 5]),('e', [21, 22])])

df = pd.DataFrame(data).T

df.plot(kind='bar', stacked=True, title="Sentiment Score for Each Company")

plt.show()