import numpy as np
import matplotlib.pyplot as plt

coin = ["heads", "tails", "side"]
number_of_throws = 100000

throws = np.random.choice(coin, number_of_throws)
np.sum(throws == "heads")
np.sum(throws == "tails")
np.sum(throws == "side")

p = [0.49165, 0.49165, 0.0167]
throws_with_p = np.random.choice(coin, number_of_throws, p=p)
print(np.sum(throws_with_p == "heads"))
print(np.sum(throws_with_p == "tails"))
print(np.sum(throws_with_p == "side"))

unique, counts = np.unique(throws_with_p, return_counts=True)
plt.bar(unique, counts)
plt.title("Coin Toss with Side landing")
plt.xlabel("Landing result")
plt.ylabel("Frequency")
plt.show()

