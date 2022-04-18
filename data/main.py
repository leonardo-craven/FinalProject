import json
 
# Opening iota file

f = open('iota.jsonl')

coordinates = []
for line in f:
    data = json.loads(line)
    coordinates.append(data['coordinates']['coordinates'])
 
# Closing file
f.close()

heights = {}
for c in coordinates:
    if (round(c[0]), round(c[1])) in heights:
        if (heights[round(c[0]), round(c[1])] > 2):
            heights[round(c[0]), round(c[1])] += .001
        else:
            heights[round(c[0]), round(c[1])] += .005
    else:
        heights[round(c[0]), round(c[1])] = .01

months = []
all_iota = []
for key in heights:
    all_iota.append(key[1])
    all_iota.append(key[0])
    all_iota.append(round(heights[key], 3))
iota = ["10/18/2019-12/01/2019", all_iota]
# print(iota)
months.append(iota)

#
#
# Opening kappa file

f = open('kappa.jsonl')

coordinates = []
for line in f:
    data = json.loads(line)
    coordinates.append(data['coordinates']['coordinates'])
 
# Closing file
f.close()

heights = {}
for c in coordinates:
    if (round(c[0]), round(c[1])) in heights:
        if (heights[round(c[0]), round(c[1])] > 2):
            heights[round(c[0]), round(c[1])] += .001
        else:
            heights[round(c[0]), round(c[1])] += .005
    else:
        heights[round(c[0]), round(c[1])] = .01

all_kappa = []
for key in heights:
    all_kappa.append(key[1])
    all_kappa.append(key[0])
    all_kappa.append(round(heights[key], 3))
kappa = ["12/01/2019-01/09/2020", all_kappa]
months.append(kappa)


##
##

# Opening lambda file

f = open('lambda.jsonl')

coordinates = []
for line in f:
    data = json.loads(line)
    coordinates.append(data['coordinates']['coordinates'])
 
# Closing file
f.close()

heights = {}
for c in coordinates:
    if (round(c[0]), round(c[1])) in heights:
        if (heights[round(c[0]), round(c[1])] > 2):
            heights[round(c[0]), round(c[1])] += .001
        else:
            heights[round(c[0]), round(c[1])] += .005
    else:
        heights[round(c[0]), round(c[1])] = .01

all_lam = []
for key in heights:
    all_lam.append(key[1])
    all_lam.append(key[0])
    all_lam.append(round(heights[key], 3))
lam = ["01/09/2020-01/26/2020", all_lam]
months.append(lam)


##
##

# Opening mu file

f = open('mu.jsonl')

coordinates = []
for line in f:
    data = json.loads(line)
    coordinates.append(data['coordinates']['coordinates'])
 
# Closing file
f.close()

heights = {}
for c in coordinates:
    if (round(c[0]), round(c[1])) in heights:
        if (heights[round(c[0]), round(c[1])] > 2):
            heights[round(c[0]), round(c[1])] += .001
        else:
            heights[round(c[0]), round(c[1])] += .005
    else:
        heights[round(c[0]), round(c[1])] = .01

all_mu = []
for key in heights:
    all_mu.append(key[1])
    all_mu.append(key[0])
    all_mu.append(round(heights[key], 3))
mu = ["01/26/2020-01/31/2020", all_mu]
months.append(mu)


##
##

# Opening nu file

f = open('nu.jsonl')

coordinates = []
for line in f:
    data = json.loads(line)
    coordinates.append(data['coordinates']['coordinates'])
 
# Closing file
f.close()

heights = {}
for c in coordinates:
    if (round(c[0]), round(c[1])) in heights:
        if (heights[round(c[0]), round(c[1])] > 2):
            heights[round(c[0]), round(c[1])] += .001
        else:
            heights[round(c[0]), round(c[1])] += .005
    else:
        heights[round(c[0]), round(c[1])] = .01

all_nu = []
for key in heights:
    all_nu.append(key[1])
    all_nu.append(key[0])
    all_nu.append(round(heights[key], 3))
nu = ["01/31/2020-02/05/2020", all_nu]
months.append(nu)


with open('all.json', 'w') as f:
    f.write(str(months))



