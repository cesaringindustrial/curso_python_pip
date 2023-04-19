
import utils
import read
import grafica

def run():
    data= read.read_csv("./app/data.csv")
    countries = list(map(lambda x: x ["Country/Territory"],data))
    percentages= list(map(lambda x: x ["World Population Percentage"],data))
    grafica.generate_pie_chart(countries,percentages)

    """
    country= input("type Country >>>")
    
    result = utils.population_by_country(data,country)
    
    if len(result) >0:
        country = result[0]
        labels, values = utils.get_population(country)
        grafica.generate_bar_chart(labels, values)
    """
  


if __name__ == '__main__':
    run()
    