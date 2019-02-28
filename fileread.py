files = ['b_lovely_landscapes.txt','c_memorable_moments.txt','d_pet_pictures.txt', 'e_shiny_selfies.txt']

for file in files:
    with open(file) as f:
        content = f.readlines()

    # Number of photos
    count = content[0]

    for x in range(1, count):
        line = content[x].split(' ')

        flip = line[0]
        number_of_tags = line[1]

        for y in range(2, number_of_tags):

        
def v_to_h(content):
    newList = []
    array = []

    for index, item in enumerate(content):
        split = str(item).split(' ')

        if(split[0] == 'H'):
            array[0] == 


    return newList



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
        
    
    if(dff1 > com):
        diff2 = diff1 - com
    else:
        diff2 = com -  diff1

    return (diff1 + com + diff2)


    







        



    



