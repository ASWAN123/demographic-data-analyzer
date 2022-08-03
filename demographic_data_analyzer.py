import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # Number of each race:
    x = df['race'].value_counts()
    race_count = x.values.tolist()


    # Average age of men:
    a1 = df.loc[df['sex'] == "Male"]
    average_age_men = round(a1['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    x1 = sum(df['education'] == 'Bachelors') / len(df)
    percentage_bachelors = round(x1*100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None



    x2 = df.loc[df['education'].isin(['Bachelors', 'Doctorate', 'Masters'] )]
    x3 = x2.loc[x2['salary'] == '>50K']
    x4 = len(x3) / len(x2)
    higher_education_rich =round(x4 * 100 , 1)  #Percentage with higher education that earn >50K


    lista_rev = ['Bachelors', 'Doctorate', 'Masters']
    y1 = df[~df.education.isin(lista_rev)]
    y2 = y1.loc[y1['salary'] == '>50K']
    y3 = len(y2) / len(y1)
    lower_education_rich = round(y3 * 100 , 1 )   #Percentage without higher education that earn >50K






    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()





    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == 1]
    z1 = num_min_workers.loc[num_min_workers['salary'] == '>50K']
    z2  = len(z1) / len(num_min_workers)
    rich_percentage = round(z2 * 100 , 1)

    #pay some  attenstion  to  this  one  
    # What country has the highest percentage of people that earn >50K?
    lista = []
    j = df['native-country'].unique()
    for  each  in j:
        j1 = df.loc[df['native-country'] == each ]
        j2 = j1[j1["salary"].str.contains('>50K')]
        if len(j2) == 0 :
            lista.append(0.0)
        else:
            j3 = len(j2) / len(j1)
            j4 = round(j3* 100, 1)
            lista.append(j4)
    highest_earning_country = j[lista.index(max(lista))]





    highest_earning_country_percentage = max(lista)

    # Identify the most popular occupation for those who earn >50K in India.
    m1 = df[df["native-country"].str.contains('India')]
    m2 = m1[m1["salary"].str.contains('>50K')]
    m3 = m2['occupation'].value_counts().idxmax()
    top_IN_occupation = m3

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
        # 'race_count': race_count, 
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



