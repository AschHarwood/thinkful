from collections import defaultdict
population_dict = defaultdict(int)

inputFile = open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'r')

header = next(inputFile)

for line in inputFile:
	line = line.rstrip().split(',')
	line[5] = int(line[5])
	if line[1] == 'Total National Population':
		population_dict[line[0]] += line[5]
inputFile.close()
 
print(population_dict)

with open('national_population.csv', 'w') as outputFile:
	outputFile.write('continent, 2010_population\n')
	for k,v in population_dict.iteritems():
		outputFile.write(k + ',' + str(v) + '\n')