import numpy as np
import pandas as pd

def calculate_demographic_data(printa_data=True):

    data = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ])

    race_count = data['race'].value_counts()

    avg_age_men = data[data['sex'] == 'Male']['age'].mean().round(1)

    percentage_bachelor = ((data['education'] == 'Bachelors').mean() * 100).round(1)

    advanced_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu_rich = ((data.loc[advanced_education, 'salary'] == '>50K').mean() * 100).round(1)

    none_education = ~advanced_education
    none_education_rich = ((data.loc[none_education, 'salary'] == '>50K').mean() * 100).round(1)

    min_hours_works = data['hours-per-week'].min()

    percentage_min_hours = ((data[data['hours-per-week'] == min_hours_works]['salary'] == '>50K').mean() * 100).round(1)

    country_earnings = data[data['salary'] == '>50K']['native-country'].value_counts()
    country_counts = data['native-country'].value_counts()
    highest_earnings_country = (country_earnings / country_counts * 100).idxmax()
    highest_earnings_country_percentage = (country_earnings / country_counts * 100).max().round(1)

    india = data['native-country'] == 'India'
    high_salary = data['salary'] == '>50K'
    top_in_occupation = data[india & high_salary]['occupation'].value_counts().idxmax()

    if printa_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", avg_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelor}%")
        print(f"Percentage with higher education that earn >50K: {higher_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {none_education_rich}%")
        print(f"Min work time: {min_hours_works} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentage_min_hours}%")
        print("Country with highest percentage of rich:", highest_earnings_country)
        print(f"Highest percentage of rich people in country: {highest_earnings_country_percentage}%")
        print("Top occupations in India:", top_in_occupation) 

    result = {
        'race_count': race_count,
        'average_age_men': avg_age_men,
        'percentage_bachelors': percentage_bachelor,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': none_education_rich,
        'min_work_hours': min_hours_works,
        'rich_percentage': percentage_min_hours,
        'highest_earning_country': highest_earnings_country,
        'highest_earning_country_percentage': highest_earnings_country_percentage,
        'top_IN_occupation': top_in_occupation
    }

    return result
