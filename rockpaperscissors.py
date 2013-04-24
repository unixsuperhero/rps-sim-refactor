import random, pylab
def throw():
    return random.choice(['rock','paper','scissors'])

def getHand():
    return [throw(), throw()]

def bothInHand(hand, one, two)
    if one in hand and two in hand
        return true
    return false

def rps(numRounds, numTrials):
    proportions = []
    for trial in range(numTrials):
        for round in range(numRounds):
            wins = {'rock': 0, 'paper': 0, 'scissors': 0, 'draw': 0}
            for hand in range(numRounds):
                hand = getHand()
                if bothInHand(hand, 'rock', 'paper'):
                    wins['paper'] += 1
                elif bothInHand(hand, 'paper', 'scissors'):
                    wins['scissors'] += 1
                elif bothInHand(hand, 'scissors', 'rock'):
                    wins['rock'] += 1
                else:
                    wins['draw'] += 1

        trialResults = {'rock': 0, 'paper': 0, 'scissors': 0, 'draw': 0}
        for k in trialResults.keys():
            trialResults[k] = wins[k] / float(numRounds)

        proportions.append(trialResults)

        print("num of rounds = "+str(numRounds)+" trial proportions = "+str(trialResults))

        #pylab.hist(proportions, bins=10, histtype='bar')
        #pylab.show()
    #print proportions
    final_props = {'rock': 0, 'paper': 0, 'scissors': 0, 'draw': 0}
    for element in proportions:
        for k in final_pros.keys()
          final_props[k] += element[k]
    for k in final_pros.keys()
      final_props[k] /= float(numTrials)
    print final_props['rock'], final_props['paper'], final_props['scissors'], final_props['draw']

rps(100,100)
