import pandas as pd

# Load US population estimates from the Census Bureau
url = "https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/state/totals/nst-est2020.csv"
population_df = pd.read_csv(url, encoding='latin1')

## Reviewing data
    # print(population_df.shape)
    # print(population_df.head())
    # print(population_df.tail())
## Exporting to CSV so I can look at actual dataset
    # population_df.to_csv("C:\\Users\\melis\\OneDrive\\Desktop\\PracticeData\\census.csv", index=False)

## Trying to filter for subset of data
    # I will filter where SUMLEV == 40 (state-level entries)
        # filtered_df = population_df[population_df['SUMLEV'] == 40] 
    # Show only NAME and CENSUS2010POP columns
        # first version attempt -- print(filtered_df[['NAME', 'CENSUS2010POP']])
    # Second attempt  = neater and without index
        # print(filtered_df[['NAME', 'CENSUS2010POP']].to_string(index=False))
    # Trying to filter on two fields: REGION == 3 and SUMLEV == 40
        # filtered_df = population_df[(population_df['REGION'] == 3) & (population_df['SUMLEV'] == 40)]
    # Getting Empty Dataset error  - remove one variable to see if just region works
        # filtered_df = population_df[population_df['REGION'] == 3] 
    # Getting Empty Dataset error - troubleshooting why
        # print(population_df['REGION'].unique())
        # print(population_df['SUMLEV'].unique())
    # Found an X in the REGION data instead of a number
    # Process to remove the X error
        # population_df['REGION'] = pd.to_numeric(population_df['REGION'], errors='coerce')
        # population_df = population_df.dropna(subset=['REGION'])
        # population_df['REGION'] = population_df['REGION'].astype(int)
        # filtered_df = population_df[(population_df['REGION'] == 3) & (population_df['SUMLEV'] == 40)]
        # print(filtered_df[['REGION', 'NAME', 'CENSUS2010POP']].to_string(index=False))
    # Success!

## Trying to filter for subset of data like ends in -ia
        # filtered_df = population_df[population_df['NAME'].str.contains('ia')]
        # print(filtered_df[['NAME']].to_string(index=False))
    # Success!

## Trying to filter for subset of data where CENSUS2010POP is between 10000 and 100000
filtered_df = population_df[(population_df['CENSUS2010POP'] >= 100000) & (population_df['CENSUS2010POP'] <= 1000000)]
        # print(filtered_df[['NAME', 'CENSUS2010POP']].to_string(index=False))
    # Success!  Now I want to sort smallest population to largest - add a sort variable
sorted_df = filtered_df.sort_values(by='CENSUS2010POP', ascending=True)
print(sorted_df[['NAME', 'CENSUS2010POP']].to_string(index=False))
    # Success!
