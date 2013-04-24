import random, pylab
def throw():
    return random.choice(['rock','paper','scissors'])

def getHand():
    return [throw(), throw()]

def bothInHand(hand, one, two)
    if one in hand and two in hand
        return true
    return false

def whoWon(hand)
    if bothInHand(hand, 'rock', 'paper'):
        return 'paper'
    if bothInHand(hand, 'paper', 'scissors'):
        return 'scissors'
    if bothInHand(hand, 'scissors', 'rock'):
        return 'rock'
    return 'draw'

def rps(numRounds, numTrials):
    proportions = []
    for trial in range(numTrials):
        for round in range(numRounds):
            wins = {'rock': 0, 'paper': 0, 'scissors': 0, 'draw': 0}
            for hand in range(numRounds):
                wins[ whoWon( getHand() ) ] += 1

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
