import pandas as pd

# make function to calculate total data for each race
def count_race(df):
    race_index = df['race'].unique()
    race_data = []

    for i in race_index:
        value = df[df['race'] == i]['race'].count() 
        race_data.append(value)

    series = pd.Series(race_data)
    return series

# make function to calculate percentage of bachelor degree
def bachelors_percentage(df):
    bachelor_count = df[df['education'] == 'Bachelors']['education'].count()
    total_count = df['education'].count()

    percentage = round((bachelor_count / total_count)*100, 1)
    return percentage

# make function to calculate total person with higher education which is entitled Bachelor, Master, or Doctorate degree
def high_education(df):
    """
    Education degree  | Education Number
    Bachelor          | 13
    Master            | 14
    Doctorate         | 16
    """
    education_num = df['education-num']
    criteria = df[((education_num == 13) | (education_num == 14) | (education_num == 16))]

    criteria_count = criteria['education'].count()
    total_count = df['education'].count()

    percentage = round((criteria_count / total_count)*100, 1)

    return criteria_count, percentage

# make function to calculate total person with lower education which is not entitled Bachelor, Master, or Doctorate degree
def low_education(df):
    """
    Education degree  | Education Number
    Bachelor          | 13
    Master            | 14
    Doctorate         | 16
    """
    education_num = df['education-num']
    criteria = df[~((education_num == 13) | (education_num == 14) | (education_num == 16))]

    criteria_count = criteria['education'].count()
    total_count = df['education'].count()

    percentage = round((criteria_count / total_count)*100, 1)

    return criteria_count, percentage

# make function to calculate percentage people with advanced/higher education who make more than 50K
def high_education_rich(function, df):
    """
    Education degree  | Education Number
    Bachelor          | 13
    Master            | 14
    Doctorate         | 16
    """
    education_num = df['education-num']
    criteria = df[((education_num == 13) | (education_num == 14) | (education_num == 16)) & (df['salary'] == '>50K')]

    criteria_count = criteria['education'].count()
    total_count, _ = function

    percentage = round((criteria_count / total_count)*100, 1)
    return percentage 

# make function to calculate percentage people without advanced/higher education who make more than 50K
def low_education_rich(function, df):
    """
    Education degree  | Education Number
    Bachelor          | 13
    Master            | 14
    Doctorate         | 16
    """
    education_num = df['education-num']
    criteria = df[~((education_num == 13) | (education_num == 14) | (education_num == 16)) & (df['salary'] == '>50K')]

    criteria_count = criteria['education'].count()
    total_count, _ = function

    percentage = round((criteria_count / total_count)*100, 1)
    return percentage 

# make function to calculate percentage people with minimum hours per week who make more than 50K
def minimum_work_rich(df):
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()

    criteria = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]

    criteria_count = criteria['hours-per-week'].count()
    total_count = num_min_workers

    percentage = round((criteria_count / total_count)*100, 1)
    return percentage 

# make function to determine what country with highest number of people who make more than 50K
def top_earning_country(df):
    selected_df = df[df['salary'] == '>50K'][['native-country','salary']]

    country_index = selected_df['native-country'].unique().tolist()
    countryman_data = []

    for i in country_index:
        value = selected_df[selected_df['native-country'] == i]['native-country'].count() 
        countryman_data.append(value)

    country_df = pd.Series(data=countryman_data, index=country_index)

    # Get the index of the row with the highest value
    max_idx = country_df.idxmax()

    return max_idx

# make function to calculate percentage of the country with highest number of people who make more than 50K from the rest
def top_earning_country_percentage(df):
    selected_df = df[df['salary'] == '>50K'][['native-country','salary']]

    country_index = selected_df['native-country'].unique().tolist()
    countryman_data = []

    for i in country_index:
        value = selected_df[selected_df['native-country'] == i]['native-country'].count() 
        countryman_data.append(value)

    country_df = pd.Series(data=countryman_data, index=country_index)

    result = round(country_df.max() / country_df.sum()*100, 1)

    return result

# make function to identify the most popular occupation for those who earn >50K in India
def top_india_occupation(df):
    selected_df = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')][['occupation','salary']]

    occ_index = selected_df['occupation'].unique().tolist()
    occ_data = []

    for i in occ_index:
        value = selected_df[selected_df['occupation'] == i]['occupation'].count() 
        occ_data.append(value)

    occupation_df = pd.Series(data=occ_data, index=occ_index)

    result = occupation_df.idxmax()
    return result

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = count_race(df)

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = bachelors_percentage(df)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = high_education(df)
    lower_education = low_education(df)

    # percentage with salary >50K
    higher_education_rich = high_education_rich(higher_education, df)
    lower_education_rich = low_education_rich(lower_education, df)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()

    rich_percentage = minimum_work_rich(df)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = top_earning_country(df)
    highest_earning_country_percentage = top_earning_country_percentage(df)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = top_india_occupation(df)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }