import json

# read json file
jsonFile = open('src\example.json', 'r')
sampleData = json.loads(jsonFile.read())

print('--------------------------------------------------')
print('UUID: ' + sampleData['uuid'])

# read true values of human, agent1, and agent2 explorations
humanSet = set(sampleData['section2']['humanExplored'])
agent1Set = set(sampleData['section2']['agent1Explored'])
agent2Set = set(sampleData['section2']['agent2Explored'])

print('True values:\n\tHuman:', len(humanSet), '\n\tAgent 1:', len(agent1Set), '\n\tAgent 2:', len(agent2Set))

# get the area explored by each individual independently
humanIndependent = humanSet.difference(agent1Set.union(agent2Set))
agent1Independent = agent1Set.difference(humanSet.union(agent2Set))
agent2Independent = agent2Set.difference(humanSet.union(agent1Set))

print('Independent values:\n\tHuman:', len(humanIndependent), '\n\tAgent 1:', len(agent1Independent), '\n\tAgent 2:', len(agent2Independent))

# get the number of victims and hazards found
obstacles = sampleData['obstacles']
numVictims, numHazards  = 0, 0
for i in obstacles:
	if i['id'] == 'victim' and i['isFound']: numVictims += 1
	elif i['id'] == 'hazard' and i['isFound']: numHazards += 1

print('Number of victims found:', numVictims, '\nNumber of hazards found:', numHazards)

# get the number of times the user integrated/discarded the explored region by each agent
decisions = sampleData['decisions']
numIntegrated, numDiscarded = 0, 0
for i in decisions['agent1']:
	if i['trusted']: numIntegrated += 1
	else: numDiscarded += 1

print('Agent 1:\n\tNumber of times integrated:', numIntegrated, '\n\tNumber of times discarded:' ,  numDiscarded)

numIntegrated, numDiscarded = 0, 0
for i in decisions['agent2']:
	if i['trusted']: numIntegrated += 1
	else: numDiscarded += 1

print('Agent 2:\n\tNumber of times integrated:', numIntegrated, '\n\tNumber of times discarded:' , numDiscarded)
print('--------------------------------------------------')
