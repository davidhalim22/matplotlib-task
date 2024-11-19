import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [5, 10, 15, 20, 25]

plt.bar(x,y, color = "#32cd32", width = 0.5, label = "Categories")
plt.grid(True, axis='x')
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart with Custom Width")

num = 0.01
for i in y:
    plt.text(num,1,i)
    num += 1

plt.grid()
plt.legend(["Categories"])
plt.savefig('plot.png')

plt.show()