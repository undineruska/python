import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating a synthetic Titanic dataset
data = {
    'PassengerId': np.arange(1, 891),
    'Survived': np.random.randint(0, 2, 890),
    'Pclass': np.random.randint(1, 4, 890),
    'Name': ['Name' + str(i) for i in range(1, 891)],
    'Sex': np.random.choice(['male', 'female'], 890),
    'Age': np.random.randint(1, 80, 890),
    'SibSp': np.random.randint(0, 6, 890),
    'Parch': np.random.randint(0, 6, 890),
    'Ticket': ['Ticket' + str(i) for i in range(1, 891)],
    'Fare': np.round(np.random.uniform(10, 300, 890), 2),
    'Cabin': [np.nan if np.random.rand() > 0.7 else 'C' + str(i) for i in range(1, 891)],
    'Embarked': np.random.choice(['C', 'Q', 'S'], 890)
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
df_head = df.head()

# Check the dimensions of the dataset
df_shape = df.shape

# Identify missing values
missing_values = df.isnull().sum()

# Compute basic statistics for numerical columns
numerical_stats = df.describe()

# Analyze categorical variables
categorical_value_counts = df.select_dtypes(include=['object']).nunique()

(df_head, df_shape, missing_values, numerical_stats, categorical_value_counts)

# Visualization of the 'Survived' column

plt.figure(figsize=(8, 6))
df['Survived'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Distribution of Survival on the Titanic')
plt.xlabel('Survived')
plt.ylabel('Number of Passengers')
plt.xticks(ticks=[0, 1], labels=['Did Not Survive', 'Survived'], rotation=0)
plt.show()
