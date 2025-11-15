#holiday robot assessment test


The exercise will have following requirements:
1. Use Python to retrieve data from a CSV file located at 
    https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/EDA14/CSV/1.0/en.
2. Select the following from that dataset:
    i. Calculate the sum of the number of females, males and both sexes having years grouped on five by five years period. Hint: The
    'VALUE' column contains numbers of students, with two distinct types
    ii. Filter for those that have the column Statistic with value containing First Year
3. Write the data in csv and parquet formats
4. Create unit tests for the functions/methods added
[Bonus] Rename all columns in lower case

Evaluation criteria
1.Design of the solution
2.Code readability
3.Code structure and organization
4.Patterns used
5.Code extensibility and reusability
6.Code documentation
7.Testing
8.Performance. It will be good to see how long every method takes

[Optional] Usage of frameworks like Docker or any other containerising solution