
import utils
import read
import grafica
import pandas as pd

def run():
    '''
    data= read.read_csv("./data.csv")
    data= list(filter(lambda item: item ["Continent"]== "South America",data))
    countries = list(map(lambda x: x ["Country/Territory"],data))
    percentages= list(map(lambda x: x ["World Population Percentage"],data))
    grafica.generate_pie_chart(countries,percentages)

    '''
    df= pd.read_csv("./data.csv")
    df= df[df['Continent']== 'Africa']
    countries= df['Country/Territory'].values
    percentages= df['World Population Percentage'].values
    grafica.generate_pie_chart(countries,percentages)
    
    data= read.read_csv("./data.csv")
    country= input("type Country >>>")
    print("country")
    result = utils.population_by_country(data,country)
    
    if len(result) >0:
        country = result[0]
        labels, values = utils.get_population(country)
        grafica.generate_bar_chart(country['Country/Territory'],labels, values)
    
  


if __name__ == '__main__':
    run()
    