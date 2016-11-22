words = userinput.split()
result = []
for words in words:
  result.appendlassify(word)
  return result

def classify(word):
  #Test if word is a direction
  #if so return ('direction', word)
if word in ('north', 'south', 'west', 'east')
    return ('direction', word)
elif word in ('go', 'kill', 'eat'):
    return ('verb', word)
elif word in ('the', 'in', 'of',)
    return ('stop', word)
elif word in ('bear', 'princess'):
    return ('noun', word)
else:
    try:
        thenumber = int(word)
        return('number', thenumber)
    except ValueError:
        #word is not a number
        return ('error', word)
    except NameError:
        #do something with a name erroe
    except Exeption:
        #do womething with any other error
 #Test if word is a verb
#if so return ('verb', word)
  #Test if word is a stop
  #if so return ('stop', word)
  #Test if word is a noun
  #if so return ('noun', word)
  #Test if word is a number
  #if so return ('number', words)
