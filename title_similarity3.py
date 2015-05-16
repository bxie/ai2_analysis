import nltk.corpus
from nltk.corpus import wordnet as wn

list_of_projects =[['test'], ['talk', 'to', 'me'], ['satelit'], ['dot'], ['list', 'picker'], ['inish'], ['paintingwithanna'], ['hospital', 'test', 'copy'], ['guard', 'dog'], ['mole', 'mash'], ['digital', 'doodle'], ['l'], ['proba'], ['talktome'], ['bob', 'marley'], ['conversor', 'de', 'moneda'], ['note', 'taker'], ['voicetalk'], ['getthegold'], ['advanced'], ['diary'], ['hello', 'purr', 'copy', 'copy'], ['no', 'texting', 'while', 'driving'], ['jump', 'jump', 'jump'], ['a'], ['kardashians'], ['bluetooth', 'app', 'send'], ['cadenas'], ['notifier'], ['test'], ['whackamole'], ['fortune', 'teller'], ['flagapp'], ['day', 'team', 'c'], ['qqqq'], ['movingball', 'a'], ['game', 'copy'], ['hellpurr', 'apk'], ['gabriel'], ['bt', 'ox', 'game', 'lab', 'v'], ['pickup'], ['compass'], ['keely', 'wright', 'hello', 'purr'], ['hello', 'purr'], ['ingzz'], ['bo'], ['fingerpainting', 'copy', 'copy'], ['casa'], ['test'], ['hello', 'purr'], ['reconocedor'], ['tech', 'squad'], ['jyh'], ['digital', 'doddle'], ['math', 'app'], ['hello', 'world'], ['esa'], ['reproductor', 'copy'], ['leon', 'huelsken'], ['paint', 'the', 'cat'], ['new'], ['pisomka'], ['dhaidclub'], ['coursework', 'app', 'copy', 'copy'], ['paint', 'pot'], ['ball', 'bounce'], ['bluetooth'], ['rh'], ['pong', 'starter'], ['first'], ['bob', 'malle'], ['paintpot'], ['test'], ['show', 'image', 'as', 'button'], ['hellopurr'], ['love'], ['quiz', 'me', 'mit'], ['editordefotos'], ['molemash'], ['email', 'gps'], ['ballbounce'], ['camera'], ['m'], ['map', 'location', 'alarm', 'clock'], ['nnw', 'command'], ['pamela'], ['revisionapp'], ['ch'], ['blah'], ['cup', 'game'], ['project'], ['talk', 'to', 'me'], ['cal'], ['golf'], ['pizza', 'party'], ['ez', 'admit', 'sue', 'copy'], ['picultimatex'], ['prime'], ['bases', 'clientes', 'lagobo'], ['talk', 'to', 'me'], ['magic', 'ball'], ['knvs', 'test'], ['get', 'the', 'gold'], ['bola'], ['funandlearn'], ['gun', 'sound'], ['bully', 'hotspot'], ['dog', 'dictionary'], ['olamundo'], ['b'], ['gps', 'sms'], ['amazon'], ['campud', 'map'], ['text', 'group'], ['paintpop'], ['talk', 'tome'], ['proj'], ['what'], ['drink'], ['doodle'], ['talk', 'to', 'me'], ['i', 'have', 'a', 'dream', 'starter'], ['mole', 'mash'], ['aaaaaaa'], ['drawerive'], ['final'], ['connect', 'fb'], ['app', 'inventor', 'mahfooza'], ['jjjj'], ['makequiztakequiz'], ['qrscan'], ['hello', 'cool', 'world'], ['aaa'], ['buttons'], ['note', 'taker', 'est'], ['boss'], ['dpnew', 'string', 'convert'], ['fare', 'calcuatr'], ['if'], ['space', 'invaders'], ['ballbounce'], ['button'], ['triaqngulo'], ['eightball'], ['texting', 'copy'], ['pong', 'starter'], ['mayor', 'num', 'li'], ['beta'], ['prueba', 'cv', 'deslizar'], ['mf'], ['balls'], ['my', 'car'], ['practica'], ['grades'], ['mypro', 'roll', 'ball'], ['meet', 'my', 'classmates'], ['control'], ['banana', 'game', 'arx'], ['xd'], ['stockquotes'], ['ballbounce', 'copy'], ['quiz'], ['test'], ['dotjoining'], ['podd'], ['t'], ['voice'], ['triviaquiz'], ['cg', 'tri', 'nac'], ['the', 'maocain', 'gameur'], ['kalori'], ['ballbounce'], ['once'], ['gcd'], ['raspored'], ['unit', 'controlled', 'assessment'], ['hajra'], ['yerson'], ['footy', 'fundamentals'], ['canvas', 'test'], ['nave'], ['malcom'], ['santana', 'exer'], ['stuff'], ['sound', 'player'], ['dice'], ['simple'], ['test'], ['picturepuzzle'], ['test'], ['bearing'], ['councilwork'], ['alumno'], ['talk', 'to', 'me', 'jm', 'part'], ['yayaya'], ['android', 'mash', 'version', 'checkpoint'], ['i', 'have', 'a', 'dream', 'starter'], ['hello', 'world'], ['guard', 'dog', 'a'], ['realsyot'], ['pong'], ['no', 'text'], ['sip'], ['math'], ['parle', 'moi'], ['garden', 'paradiso', 'v'], ['deneme'], ['rassel', 'ballbounce'], ['new'], ['parking', 'directions'], ['practica'], ['infinityblade'], ['app'], ['fun', 'fun'], ['prueba'], ['kjn'], ['games', 'app'], ['the', 'lakeside', 'hammers'], ['movement', 'with', 'sensors'], ['project'], ['digital', 'doodle'], ['ball', 'game'], ['magic', 'ball', 'v'], ['mr', 'felipe'], ['pic', 'call'], ['art'], ['phonenumber'], ['bmi']]


## helper function
def getNewWordSyn(word, singular):
	singularStr = str(singular)
	wordSynsets = wn.synsets(word)
	newWord 		= ''
	wordType    = "%s " % (wordSynsets[0].lexname())
	if wordType[2]   == 'u': #no(u)n
		newWord  = singularStr + '.n.01'
	elif wordType[2] == 'j': #ad(j)
		newWord  = singularStr + '.a.01'
	elif wordType[2] == 'r': #ve(r)b
		newWord  = singularStr + '.v.01'
	elif wordType[2] == 'v': #ad(v)erb
		newWord  = singularStr + '.r.01'
	else:
		pass
	newWordSyn = wn.synset(newWord) 
	return newWordSyn

def getMaxSimilarity(somelist):
	uncounted_words = [] 
	perfect_match   = [] 
	words_max_score = {} 

	for i in range(len(somelist)):
		if i == len(somelist)-1: #if the last sublist, do not compare
			break
		title_former  = somelist[i]

		maxSimilarity = 0
		maxWord1 	  = ''
		maxWord2      = ''
		for word in title_former:
			singular = wn.morphy(word) #convert to singular
			# print word, singular
			if singular == None:
				pass 
			elif singular != None:
				newWordSyn  = getNewWordSyn(word,singular)
				if not newWordSyn:
					uncounted_words.append(word)
					continue
				else:
					for j in range(i+1,len(somelist)):
						title_latter = somelist[j]
						for word1 in title_latter:
							singular1 = wn.morphy(word1) 
							if singular1 == None:
								pass
							elif singular1 != None:
								newWordSyn1  	 = getNewWordSyn(word1,singular1)
								tempSimilarity  = newWordSyn.wup_similarity(newWordSyn1)

								if tempSimilarity== None: 
									uncounted_words.append((word,word1))
								else:
									if tempSimilarity== 1:
										perfect_match.append((word,word1))
									else:
										if tempSimilarity>maxSimilarity:
											maxSimilarity = tempSimilarity
											maxWord1      = word
											maxWord2      = word1
		words_max_score[(maxWord1,maxWord2)]     =  maxSimilarity 

	return [words_max_score,perfect_match,uncounted_words]

somesim = getMaxSimilarity(list_of_projects)

print somesim[1]
# print len(somesim[2])
				

   

