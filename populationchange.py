from collections import defaultdict
population_dict2010 = defaultdict(float)
population_dict2100 = defaultdict(float)
population_dictchange = defaultdict(float)
population_dictratechange = defaultdict(float)

inputFile = open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'r')

header = next(inputFile)

for line in inputFile:
	line = line.rstrip().split(',')
	line[6] = float(line[6]) #converts 2100 population to float
	line[5] = float(line[5]) #converts 2010 population to float
	if line[1] == 'Total National Population': #looks for rows with total pop
		population_dict2010[line[0]] += line[5] #adds rural and urban in 210
		population_dict2100[line[0]] += line[6] #add rural and urban in 2100
population_dictchange = {key: population_dict2100[key] - population_dict2010.get(key, 0) for key in population_dict2100.keys()} #finds abosulte change in population
population_dictratechange = {key: ((population_dictchange[key] / population_dict2010.get(key, 0))*100) for key in population_dictchange.keys()}
inputFile.close()
 
print(population_dictratechange)
print max(population_dictratechange, key=population_dictratechange.get)

#with open('national_population.csv', 'w') as outputFile:
#	outputFile.write('continent, 2010_population\n')
#	for k,v in population_dict.iteritems():
#		outputFile.write(k + ',' + str(v) + '\n')