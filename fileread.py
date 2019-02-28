import time

#files = ['b_lovely_landscapes.txt','c_memorable_moments.txt','d_pet_pictures.txt', 'e_shiny_selfies.txt']
files = ['b_lovely_landscapes.txt']


def v_to_h(content):
    newList = []

    #Horizontal to list
    for index, line in enumerate(content):
        if index != 0:
            
            array = []
            items = str(line).split(' ')
            if(items[0] == 'H'):
                array.append(index)
                array.append(0)

                for i, tag in enumerate(items):
                    if i != 0 and i != 1:
                        array.append(tag)

            newList.append(array)

    return newList


for file in files:
    with open(file) as f:
        content = f.readlines()

    newList = v_to_h(content)


def Score(pic1, pic2):
    score = 0

    tags1 = pic1[-(len(pic1)-2)]
    tags2 = pic2[-(len(pic2)-2)]

    diff1 = 0
    diff2 = 0
    com = 0

    for tag1 in tags1:
        isCom = False
        for tag2 in tags1:
            if tag1 == tag2:
                isCom = True
            
        if isCom:
            com = com + 1
        else:
            diff1 = diff1 + 1
        
    
    if(diff1 > com):
        diff2 = diff1 - com
    else:
        diff2 = com -  diff1

    return min([diff1,diff2,com])


def Order(listofslides):
	sequence = []
	newlistofslides = listofslides
	score = 0
	index = 0
	while len(newlistofslides) != 0:
		curr_slide =newlistofslides[index]
		rest = newlistofslides.remove(newlistofslides[i])
		next_index,curr_score= Bestscore(x,rest)
		sequence.append(newlistofslides[next_index])
		score += curr_score
		index = next_index


	return sequence, score


def Bestscore(slide,listofslides):
	curr_score = 0
	best_score = 0
	index = 0
	for i in range(len(listofslides)):
		curr_score = Score(slide,listofslides[i])
		if curr_score >= best_score:
			best_score = curr_score
			index = i

	return index, best_score