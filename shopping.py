import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')
days = [1, 2, 3]
laptop = [27, 12, 38]
mouse = [56, 85, 43]
keyboard = [13, 35, 23]

index = np.arange(len(days))
height = 0.2
plt.barh(index - height, 
        laptop,
        color = 'y',
        height=height,
        label='laptop sales')

plt.barh(index,
        mouse,
        color= 'red',
        height= height,
        label='mouse sales')

plt.barh(index + height, 
        keyboard,
        color='blue',
        height= height,
        label='keyboard sales')

plt.yticks(ticks= index, labels= days)
plt.legend()

plt.title("computer store sales information")
plt.xlabel("sales")
plt.ylabel("days")


plt.show()