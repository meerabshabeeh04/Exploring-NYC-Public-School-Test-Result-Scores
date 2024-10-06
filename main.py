import pandas as pd
schools = pd.read_csv("schools.csv")
# Preview the first few rows of the data to understand its structure
schools.head()
# Filter schools that have an average math score of at least 640 (80% of the max score of 800)
best_math = schools[schools['average_math'] >= 640].sort_values('average_math', ascending=False)
# Create a DataFrame containing the school names and their corresponding average math scores, sorted in descending order
best_math_schools = best_math[['school_name', 'average_math']]
print(best_math_schools.head())
# Calculate the total SAT score by summing up the average math, reading, and writing scores for each school
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
# Sort the schools based on the total SAT score in descending order
sorted_school = schools.sort_values('total_SAT', ascending=False)
# Select the top 10 performing schools based on the combined total SAT score, including their names and total SAT scores
top_10_schools = sorted_school[['school_name', 'total_SAT']].head(10)
print(top_10_schools)
# Group the schools by borough and calculate the number of schools, the mean, and the standard deviation of total SAT scores for each borough
boroughs = sorted_school.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
# Identify the borough that has the largest standard deviation in total SAT scores
large_std_dev = boroughs[boroughs['std'] == boroughs['std'].max()]
# Rename columns for clarity: number of schools, average SAT score, and standard deviation of SAT scores
largest_std_dev = large_std_dev.rename(columns={"count": 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'})
# Print the borough with the largest standard deviation of SAT scores
print(largest_std_dev.head())
