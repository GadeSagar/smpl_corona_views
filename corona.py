
import COVID19Py

import matplotlib.pyplot as mpl

covid19 = COVID19Py.COVID19()

data = covid19.getAll(timelines=True)

virusdetails1 = dict(data["latest"])

names = list(virusdetails1.keys())

values = list(virusdetails1.values())

mpl.bar(range(len(virusdetails1)), values, tick_label = names)

print(virusdetails1)

mpl.show()


