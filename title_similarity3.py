import nltk.corpus
from nltk.corpus import wordnet as wn

list_of_projects= [['space', 'invaders'], ['draw'], ['flaggenerator'], ['paint', 'pot', 'random'], ['pongkeyur'], ['image'], ['app', 't'], ['zombie', 'locatoe'], ['hello', 'world'], ['spaceship'], ['voiceit'], ['ahmedmero'], ['aaaaa'], ['novo', 'aplicativo', 'copy'], ['hello', 'miaw', 'miaw'], ['pippo'], ['p'], ['retriever'], ['lists'], ['digital', 'doodle'], ['project', 'disha', 'linda'], ['dankalys'], ['dibujar'], ['paint', 'pot'], ['molemash'], ['aaa'], ['calculatrice', 'complexe'], ['map', 'it', 'displaying', 'locationsona', 'google', 'map'], ['mole', 'mash'], ['test', 'app'], ['getthe', 'gold'], ['t'], ['pieridis', 'museum', 'copy'], ['ping', 'pong'], ['talking', 'robot', 'copy'], ['footy', 'app'], ['piano'], ['zayed'], ['coin', 'flip', 'media', 'only', 'copy'], ['in', 'and', 'out', 'startdragndraw'], ['dontshakeme'], ['dexterity', 'new'], ['aaa'], ['bluttoth', 'conference'], ['whack', 'a', 'mole'], ['timer'], ['falling'], ['ball'], ['colora'], ['android', 'mash', 'project'], ['test'], ['take', 'quiz', 'va'], ['file', 'by', 'file', 'drive'], ['petete'], ['paint', 'checkpoint', 'checkpoint'], ['test', 'dialogue', 'copy'], ['qwe'], ['cassidy', 'animation'], ['test'], ['gustavo'], ['npf'], ['msa'], ['esas'], ['app', 'thing'], ['share', 'screens'], ['ping', 'pong'], ['text'], ['klingel'], ['mole', 'mash'], ['final'], ['t'], ['pizza', 'party', 'mit'], ['b', 'ex'], ['v', 'ive', 'latino', 'faro'], ['hello', 'me'], ['test'], ['gps'], ['mysql'], ['coachman', 'biology', 'quiz'], ['mole', 'mash'], ['qwdqwd'], ['bluetooth', 'connection', 'whatakuai'], ['tinywebdb'], ['peso', 'ideale'], ['lapocalisse'], ['two', 'screens'], ['bounceball'], ['ergo', 'time', 'copy'], ['hello', 'purr'], ['final', 'project'], ['signarutas'], ['list', 'example'], ['animation'], ['agenda'], ['animal', 'sounds'], ['project'], ['test'], ['moutain'], ['f', 'cgraus'], ['to', 'do', 'list', 'v'], ['kerst', 'game'], ['task'], ['donsfirst'], ['koraan', 'karem'], ['fusiontable'], ['project'], ['appinventor'], ['captura', 'hora'], ['factorial'], ['high', 'low', 'dice', 'game'], ['text', 'to', 'speech'], ['ex'], ['mole', 'mash'], ['talktome'], ['rep', 'max'], ['buscaminas'], ['drum', 'play'], ['paint', 'pot'], ['calcolatrice'], ['paint', 'pot', 'copy', 'final'], ['mapingourworld'], ['blue', 'tooth', 'test'], ['dudewheresmcar'], ['ateologia'], ['pasword'], ['talktome'], ['hello', 'purr'], ['brujula'], ['paint', 'pot'], ['gps'], ['app'], ['tntwkwmdrka'], ['numbers', 'game'], ['virtual', 'pet'], ['first'], ['lwh'], ['proplayerxdxd'], ['tutorial', 'eng', 'simple', 'radio'], ['s', 'final'], ['bluetooh', 'controller'], ['superawesomedrawer'], ['note', 'app'], ['guitar', 'tuner'], ['practice'], ['network', 'performance'], ['h'], ['ball', 'bounce'], ['cse'], ['test'], ['escape'], ['seerecord'], ['app'], ['google', 'maps'], ['shake'], ['fusion', 'tables'], ['ball', 'bounce'], ['ball'], ['day'], ['test'], ['talk', 'to', 'me'], ['preuve'], ['alltheapps'], ['thefirstapp', 'copy'], ['hernandezperro'], ['proyectoprueba'], ['rafa'], ['automacao', 'casa', 'v'], ['spaceinvaders'], ['first', 'app'], ['fad'], ['p'], ['a'], ['ball', 'bounce'], ['storage'], ['par', 'impar'], ['sports', 'app'], ['kitty'], ['daniel', 'aksel', 'dahlgaard', 'petersen', 'spilprojekt', 'daniel', 'charlotte'], ['doodle', 'copy'], ['paris', 'map', 'tour'], ['proyectcirculos'], ['viveres', 'v'], ['new', 'ball', 'copy'], ['paintpot', 'adrianvalentin'], ['b'], ['practice'], ['mmc', 'v'], ['union'], ['toons', 'anna', 'ramsey'], ['cihuy'], ['pong'], ['proyecto', 'gps', 'leslie'], ['prova'], ['smartcat'], ['aisha'], ['bw'], ['exercicio'], ['drawing', 'game'], ['video', 'wall'], ['nestedlistpicker'], ['ex'], ['harso'], ['ahrens', 'calculator', 'hr'], ['ipman'], ['mole', 'mash'], ['i', 'have', 'a', 'dream', 'final'], ['meowmeow'], ['know', 'your', 'presidents'], ['testapp'], ['hola', 'mundo'], ['bigu'], ['button', 'talk'], ['hands'], ['thank', 'you', 'mr', 't'], ['paint', 'pot'], ['core', 'linterna', 'v', 'copy'], ['jemmmas'], ['myapp'], ['time'], ['ball', 'bounce'], ['cuestionarios'], ['inquiry'], ['darknight'], ['talktome'], ['calculadora'], ['dog'], ['presidents', 'quiz'], ['mole', 'hole'], ['test'], ['flung'], ['app', 'inventor'], ['logo', 'no', 'params', 'template'], ['program'], ['betty'], ['project', 'mush'], ['game'], ['test'], ['erpapp'], ['termox', 'copy'], ['shopping', 'list'], ['jsq'], ['lesson'], ['paint', 'pot'], ['senal'], ['elbelkassy'], ['soundboard'], ['talk', 'to', 'me'], ['gemba', 'checkpoint'], ['bluetooth', 'chat'], ['talk', 'to', 'me'], ['marching', 'band', 'memes'], ['d', 'bdatabase'], ['aa'], ['dld', 'ptmf'], ['bad', 'ti', 'ceps'], ['guard', 'dog'], ['resume', 'tracker', 'new', 'design', 'checkpoint'], ['flag', 'genorater'], ['space', 'invadors'], ['dnme'], ['appi', 'nv'], ['drivefusion', 'modified'], ['scex'], ['digitaldoodle'], ['hello'], ['test'], ['mini', 'project', 'lambo'], ['macig', 'ball'], ['dice'], ['aquario'], ['practice'], ['ball', 'bounce'], ['montacargas', 'copy'], ['carmensita'], ['start'], ['test', 'app'], ['b', 'copy'], ['ex', 'list', 'picker'], ['drawline'], ['talk', 'to', 'me', 'advance'], ['bluetooth', 'stuff'], ['conf', 'cloud'], ['ggbainin'], ['quiz'], ['mp', 'youtube'], ['n'], ['dialogs'], ['yafeelsogood'], ['pizza'], ['foodiri'], ['mitosis'], ['pou'], ['test'], ['birdy', 'copy'], ['test'], ['text'], ['project'], ['library', 'scavenger', 'hunt'], ['kd', 'app'], ['dawood', 'project'], ['t', 'hello', 'cat'], ['mini', 'golf', 'mit'], ['where', 'is', 'my', 'car'], ['test', 'copy', 'copy'], ['conoceme'], ['aaa'], ['talkto', 'me'], ['starcatcher'], ['message'], ['ball', 'of', 'la', 'bounca'], ['hola', 'cetis'], ['piplacol'], ['magic', 'ball', 'copy', 'copy'], ['piano'], ['ask'], ['home', 'alarm', 'clock'], ['mao'], ['i', 'have', 'a', 'dream', 'starter'], ['danny'], ['coin', 'flip', 'projects'], ['mole', 'mash'], ['arduino'], ['lists'], ['animathlearning'], ['receive'], ['map'], ['signal'], ['kubala'], ['shooting'], ['caber', 'neo'], ['paint', 'pot'], ['app'], ['space', 'invaders'], ['miprimera', 'app'], ['molemash'], ['a'], ['first', 'app'], ['combustivel'], ['henry'], ['work'], ['sports'], ['three', 'language'], ['clasificados'], ['gps'], ['midexam'], ['b'], ['ball', 'bounce'], ['i', 'have', 'a', 'dream', 'starter'], ['magic', 'eight', 'ball'], ['chapter', 'paint'], ['viewer'], ['ball'], ['presidents', 'quiz'], ['jims'], ['prova'], ['hyper', 'copy'], ['get', 'the', 'gold'], ['ponpon'], ['gsce', 'app'], ['animals'], ['my', 'first', 'app'], ['blog'], ['ctu'], ['thec', 'hello', 'purr'], ['talk', 'to', 'me'], ['tp'], ['test'], ['app', 'myself'], ['hello', 'purr'], ['show'], ['firstapp'], ['informa', 't'], ['patiphan'], ['ball'], ['cookie', 'clicker'], ['the'], ['jumping', 'ball'], ['tilt', 'to', 'move'], ['bricks', 'copy'], ['juego'], ['advent', 'calender'], ['file', 'by', 'file', 'google', 'drive', 'auto', 'lists'], ['gyro', 'game'], ['w', 'ow'], ['carcar'], ['i', 'bot'], ['hong'], ['connect', 'android'], ['app'], ['webpic'], ['lololololololol'], ['test', 'copy'], ['bbsit'], ['weddingapp'], ['viewer'], ['geo', 'cache', 'money'], ['coucou', 'copy'], ['guziki'], ['hello', 'gatsby', 'm', 'castano', 'checkpoint'], ['hehehe'], ['tts'], ['table'], ['potato'], ['s', 'wor', 'd'], ['pong', 'game'], ['test'], ['talk', 'to', 'me'], ['c', 'copy'], ['examen', 'app', 'turistica'], ['new'], ['paintpot'], ['animals'], ['taller', 'v'], ['sol'], ['get', 'the', 'gold'], ['t', 'mariquita'], ['delhi'], ['snake', 'v', 'copy'], ['quiz'], ['pintura'], ['healthy', 'basketsgame'], ['fish'], ['ulises'], ['prototype'], ['text', 'to', 'voice'], ['oekaki'], ['bn', 'music', 'player', 'lab'], ['sj'], ['textvoice'], ['ap', 'mole', 'mash'], ['paint', 'pot'], ['nxt', 'remote'], ['shooter'], ['android', 'mash'], ['london', 'map', 'tour'], ['a'], ['thing'], ['boitasson'], ['connecting', 'to', 'ou'], ['digital', 'doodle'], ['vallejohernandezc'], ['tablet'], ['ex', 'even', 'sum'], ['test'], ['test'], ['b', 'mind'], ['childrens', 'contact', 'list'], ['aula'], ['no'], ['despachos', 'copy'], ['paint', 'pot'], ['merged'], ['promosso', 'bocciato'], ['amy'], ['flyfish'], ['pallina'], ['multipantalla'], ['dc', 'sos'], ['onde', 'estou'], ['amazon', 'at', 'the', 'bookstore'], ['zelda'], ['collect', 'the', 'balls'], ['tre'], ['ball', 'bounce'], ['cotacao'], ['mid', 'u'], ['marley'], ['labyrinth'], ['hw', 'game'], ['masha'], ['koscom', 'app'], ['luvi'], ['euclid'], ['demo', 'alr'], ['examen'], ['myfirstapp'], ['telecomandorobot', 'lego'], ['url'], ['new'], ['pikachu'], ['karly'], ['ara', 'h', 'ok'], ['digital', 'doodle'], ['ballbounce'], ['piramide'], ['sutherland', 'project', 'part'], ['slop', 'watch', 'no', 'sum', 'splits', 'last', 'stable'], ['tiny', 'web', 'db', 'template'], ['new', 'project', 'quiz'], ['proyecto'], ['mali'], ['test'], ['rocket', 'sprite'], ['myquiz'], ['bluetooth', 'connection', 'ai', 'whatakuai'], ['ball', 'bounce'], ['get', 'the', 'gold'], ['universitymap', 'checkpoint'], ['gamb', 'app'], ['arduino']]
uncounted_words = [] 
perfect_match   = [] 
words_max_score = {} 

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

	for i in range(len(somelist)):
		if i == len(somelist)-1: #if only sublist, do not compare
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
				else:
					for j in range(i+1,len(somelist)):
						title_latter = somelist[j]
						for word1 in title_latter:
							singular1 = wn.morphy(word1) 
							if singular1 == None:
								uncounted_words.append(word1)
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

	return words_max_score

print getMaxSimilarity(list_of_projects)

#two things:
# fix the 1 thing by checking with smaller input
# re-test similarities for the one > 0.5 - does it say anything?
# percentage of tutorials.






				

   

