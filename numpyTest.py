import numpy as np
from matplotlib import pyplot as plt

a = np.arange(0, 10, 1)
print(a)

x = [1, 2, 3, 4]
y = [10, 12, 13, 15]

plt.xlabel("Age")
plt.ylabel("No of person")
plt.title("Biodata")
# plt.plot(x, y, label="Men")
# plt.plot([1, 2, 3, 4], [5, 8, 13, 18], label="Women")
plt.bar(x, y, label="Men")
plt.bar([1, 2, 3, 4], [5, 8, 13, 18], label="Women")
plt.legend()
plt.show()
