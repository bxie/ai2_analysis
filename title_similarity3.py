import nltk.corpus
from nltk.corpus import wordnet as wn

uncounted_words = [] 
perfect_match   = [] 
words_max_score = {} 

for i in range(len(list_of_projects)):
	if i == len(list_of_projects)-1: #if only sublist, do not compare
		break
	title_former = list_of_projects[i]

	maxSimilarity = 0
	maxWord1 	  = ''
	maxWord2      = ''
	for word in title_former:
		singular = wn.morphy(word) #convert to singular
		# print word, singular
		if singular == None:
			uncounted_words.append(word)

		elif singular != None:

			singularStr = str(singular)
			wordSynsets = wn.synsets(word)
			wordType = "%s " % (wordSynsets[0].lexname())
			if wordType[2]   == 'u': #no(u)n
				newWord = singularStr + '.n.01'
			elif wordType[2] == 'j': #ad(j)
				newWord = singularStr + '.a.01'
			elif wordType[2] == 'r': #ve(r)b
				newWord = singularStr + '.v.01'
			elif wordType[2] == 'v': #ad(v)erb
				newWord = singularStr + '.r.01'
			else:
				print "herro"

			newWordSyn = wn.synset(newWord) 
			if not newWordSyn:
				print "not newwordsyn, continuing"
				uncounted_words.append(word)
				continue 

			for j in range(i+1,len(list_of_projects)):
				title_latter = list_of_projects[j]
				for word1 in title_latter:
					singular1 = wn.morphy(word1) 

					if singular1 == None:
						uncounted_words.append(word1)
					elif singular1 != None:
						singularStr1 = str(singular1)
						wordSynsets1 = wn.synsets(word1)
						wordType1 = "%s " % (wordSynsets1[0].lexname())
						if wordType1[2]   == 'u':
							newWord1 = singularStr1 + '.n.01'
						elif wordType1[2] == 'j':
							newWord1 = singularStr1 + '.a.01'
						elif wordType1[2] == 'r':
							newWord1 = singularStr1 + '.v.0'
						elif wordType1[2] == 'v':
							newWord1 = singularStr1 + '.r.01'

						newWordSyn1     = wn.synset(newWord1)
						tempSimilarity  = newWordSyn.wup_similarity(newWordSyn1)

						if tempSimilarity   == None: 
							uncounted_words.append((word,word1))
						else:
							if tempSimilarity > maxSimilarity:
								maxSimilarity = tempSimilarity
								maxWord1 = word
								maxWord2 = word1
	words_max_score[(maxWord1,maxWord2)] =  maxSimilarity

print "words_max_score", words_max_score








				

   

