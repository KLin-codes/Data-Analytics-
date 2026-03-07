import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("/Users/k.lin/Documents/Documents - Kenny's MacBook Pro/Codes/csv/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    total = df.shape[0]
    with_bachelor = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = (with_bachelor / total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    selected = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')].shape[0]
    more_than = df[(df['education'].isin(['Bachelor', 'Master', 'Doctorate'])) & (['salary'] == '>50K')].shape[0]
    higher_education_rich = (more_than/selected) *100

    # What percentage of people without advanced education make more than 50K?
    low_education = df[(~ df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))]
    more_than_50 = low_education[low_education['salary'] == '>50K'].shape[0]
    lower_education_rich = (more_than_50/low_education.shape[0]) *100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    have_more_than_50K = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = (have_more_than_50K/num_min_workers.shape[0]) *100

    # What country has the highest percentage of people that earn >50K?
    count_per_country = df['native-country'].value_counts()
    rich_ppl_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_per_country = (rich_ppl_count/count_per_country) *100
    highest_earning_country = percentage_per_country.idxmax()
    highest_earning_country_percentage = percentage_per_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    rich_from_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts()
    top_IN_occupation = rich_from_occupation.idxmax()

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