def fibonacci_generator():
  """
  This generator function yields Fibonacci numbers indefinitely.

  Yields:
      int: The next Fibonacci number in the sequence.
  """
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

def get_fibonacci_number(n):
  """
  This function efficiently calculates the nth Fibonacci number using a generator.

  Args:
      n (int): The index of the desired Fibonacci number.

  Returns:
      int: The nth Fibonacci number.
  """
  if n < 0:
    raise ValueError("n must be non-negative")
  gen = fibonacci_generator()
  for _ in range(n):
    fib_number = next(gen)
  return fib_number

if __name__ == "__main__":
  while True:
    try:
      # Get user input for the Fibonacci sequence length (positive integer)
      n = int(input("Enter the length of the Fibonacci sequence (positive number): "))
      if n <= 0:
        print("Invalid input. Please enter a positive number.")
        continue

      # Get user input for the desired Fibonacci number index (within sequence length)
      while True:
        try:
          m = int(input(f"Choose a number from 1 to {n} in the sequence: "))
          m = m+1
          if 0 <= m < n:
            break
          else:
            print(f"Invalid input. Please enter a number between 1 and {n}.")
        except ValueError:
          print("Invalid input. Please enter an number.")

      break  # Exit the loop if valid inputs are received

    except ValueError:
      print("Invalid input. Please enter a positive number for sequence length.")

  # Calculate and print the desired Fibonacci number efficiently
  fib_number = get_fibonacci_number(m)
  print(f"The {m}th Fibonacci number in the sequence of length {n} is: {fib_number}")
