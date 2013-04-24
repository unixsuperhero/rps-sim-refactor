import random, pylab
def throw():
    return random.choice(['rock','paper','scissors'])

def getHand():
    return [throw(), throw()]

def rps(numRounds, numTrials):
    proportions = []
    for trial in range(numTrials):
        for round in range(numRounds):
            results = []
            for hand in range(numRounds):
                hand = getHand()
                if 'rock' in hand and 'paper' in hand:
                    results.append('paper')
                elif 'paper' in hand and 'scissors' in hand:
                    results.append('scissors')
                elif 'scissors' in hand and 'rock' in hand:
                    results.append('rock')
                else:
                    results.append('draw')
            rock = 0
            paper = 0
            scissors = 0
            draw = 0
            for result in results:
                if result == 'rock':
                    rock += 1
                elif result == 'paper':
                    paper += 1
                elif result == 'scissors':
                    scissors += 1
                else:
                    draw += 1
        trialResults = []
        rockProportion = rock/float(numRounds)
        trialResults.append(rockProportion)
        paperProportion = paper/float(numRounds)
        trialResults.append(paperProportion)
        scissorsProportion = scissors/float(numRounds)
        trialResults.append(scissorsProportion)
        drawProportion = draw/float(numRounds)
        trialResults.append(drawProportion)
        proportions.append(trialResults)
        print("num of rounds = "+str(numRounds)+" trial proportions = "+str(trialResults))

        #pylab.hist(proportions, bins=10, histtype='bar')
        #pylab.show()
    #print proportions
    rockProportion = 0
    paperProportion = 0
    scissorsProportion = 0 
    drawProportion = 0
    for element in proportions:
        rockProportion += element[0]
        paperProportion += element[1]
        scissorsProportion += element[2]
        drawProportion += element[3]
    rockProportion /= float(numTrials)
    paperProportion /= float(numTrials)
    scissorsProportion /= float(numTrials)
    drawProportion /= float(numTrials)
    print rockProportion, paperProportion, scissorsProportion, drawProportion

rps(100,100)
