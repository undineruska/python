def count_coins(amount):  # Function to calculate coin breakdown for a given amount
  """
  This function takes an amount in cents and calculates the number of coins of each denomination (50, 20, 10, 5, 2, 1) needed to represent that amount.

  Args:
      amount (int): The amount in cents to be converted into coins

  Returns:
      dict: A dictionary containing coin denominations (keys) and their corresponding counts (values)
  """
  coins = [50, 20, 10, 5, 2, 1]  # Supported coin denominations (descending order)
  coin_count = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}  # Dictionary to store coin counts (initially 0 for all)

  for coin in coins:  # Iterate through each coin denomination
    if amount >= coin:  # Check if remaining amount is enough for current coin
      """
      Calculate the number of coins needed for the current denomination and update the coin count dictionary.
      """
      coin_count[coin] = amount // coin
      amount = amount % coin  # Update remaining amount after using current denomination

  return coin_count  # Return the dictionary with final coin counts

amount_in_cents = 20099  # Amount to be converted into coins
result = count_coins(amount_in_cents)  # Get coin breakdown for the amount

for coin, count in result.items():  # Loop through coin denominations and counts
  print(f"{coin} cent coin: {count} pieces")  # Print formatted output with coin details
