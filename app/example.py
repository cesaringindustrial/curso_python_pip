import utils
import read
import grafica



def run():
    data= read.read_csv("./app/data.csv")
    column= "World Population Percentage"
    
    result = utils.population_by_country(data,country)
    
    if len(result) >0:
        country = result[0]
        labels, values = utils.get_population(country)
        grafica.generate_bar_chart(labels, values)
    
    print(result)
        
if __name__ == '__main__':
    run()    
