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
            wins = {'rock': 0, 'paper': 0, 'scissors': 0, 'draw': 0}
            for hand in range(numRounds):
                hand = getHand()
                if 'rock' in hand and 'paper' in hand:
                    wins['paper'] += 1
                elif 'paper' in hand and 'scissors' in hand:
                    wins['scissors'] += 1
                elif 'scissors' in hand and 'rock' in hand:
                    wins['rock'] += 1
                else:
                    wins['draw'] += 1

        trialResults = []
        rockProportion = wins['rock']/float(numRounds)
        trialResults.append(rockProportion)
        paperProportion = wins['paper']/float(numRounds)
        trialResults.append(paperProportion)
        scissorsProportion = wins['scissors']/float(numRounds)
        trialResults.append(scissorsProportion)
        drawProportion = wins['draw']/float(numRounds)
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
