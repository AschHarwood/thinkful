import collections
population_dict = collections.defaultdict(int) #creates a dictionary
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile) #saves the top row as a header
    for line in inputFile:
    	line = line.rstrip().split(',') # for each line in csv, strips spaces and then adds comma
    	line[5] = int(line[5]) #converts to an int
    	if line[1] == 'Total National Population':
    		population_dict[line[0]] += line[5] #adds up all the values in line 5
print(population_dict)
