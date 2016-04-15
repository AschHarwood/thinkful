from collections import defaultdict
population_dict2010 = defaultdict(float)
totallandarea_dict = defaultdict(float)
popdensity_dict = defaultdict(float)

inputFile = open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'r')

header = next(inputFile)

for line in inputFile:
	line = line.rstrip().split(',')
	line[5] = float(line[5]) #converts 2010 population to float
	line[7] = float(line[7]) #converts land area to float
	if line[1] == 'Total National Population': #looks for rows with total pop
		population_dict2010[line[0]] += line[5] #adds rural and urban in 210
		totallandarea_dict[line[0]] += line[7] # adds rural and urban land area
popdensity_dict = {key: population_dict2010[key] / totallandarea_dict.get(key, 0) for key in population_dict2010.keys()} #finds abosulte change in population

inputFile.close()
 
print(popdensity_dict)
print max(popdensity_dict, key=popdensity_dict.get)

#with open('national_population.csv', 'w') as outputFile:
#	outputFile.write('continent, 2010_population\n')
#	for k,v in population_dict.iteritems():
#		outputFile.write(k + ',' + str(v) + '\n')