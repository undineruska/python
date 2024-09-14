import numpy as np
import sys

coin = ["Heads", "Tails"]
number_of_throws = 1000

tosses = np.random.choice(coin, number_of_throws)
print (f"Resultes of coin tosses: {number_of_throws} {tosses}")

nr_heads = np.sum(tosses == "Heads")
nr_tails = np.sum(tosses == "Tails")
prob_heads = nr_heads/number_of_throws
prob_tails = nr_tails/number_of_throws
print (f"Probability of heads: {prob_heads}")
print (f"Probability of tails: {prob_tails}")



