# vignere

* Vignere encoding modified from http://invpy.com/vigenereCipher.py 
* Extended to work with Danish letters
* Added code to do frequency analysis for decoded string with a period parameter
* 


./vignere.py -h
usage: vignere.py [-h] [--encrypt] [--decrypt] [--text TEXT] [--key KEY]
                  [--period PERIOD]

Vignere Cipher with Danish Alphabet

optional arguments:
  -h, --help       show this help message and exit
  --encrypt        use to encrypt a text
  --decrypt        use to decrypt a text
  --text TEXT      text to encrypt or decript
  --key KEY        key to encrypt with
  --period PERIOD  take input text and split in "period" strings

Example

./vignere --period 3 --key ASK --encrypt --text '''Hvor det dog kedede Alice at sidde sammen med søsteren dernede ved søen - uden at have noget at tage sig til! Et par gange havde hun kigget i den bog, søsteren var i færd med at læse, men der var ingen billeder i den og heller ingen samtaler ...  "Og hvad fornøjelse har man af en bog uden billeder, og hvor personerne ikke snakker med hinanden?" tænkte Alice.  Man kunne jo give sig til at binde kranse, men var det så morsomt, at det var umagen værd at rejse sig op og plukke bellis? Mens Alice således sad og tænkte frem og tilbage (så godt hun kunne på grund af varmen, der gjorde hende sløv og søvnig) - opdagede hun pludselig en hvid kanin med røde øjne. Den løb lige forbi hende ...  Det var ikke særlig mærkværdigt, og Alice syntes heller ikke, det var særlig overraskende, at kaninen sagde til sig selv: "Ih, du glade verden! Jeg kommer for sent - Da hun tænkte på det bagefter, syntes Side 2 af 57 hun ganske vist, at hun burde være blevet forbavset, men lige i øjeblikket betragtede hun det som noget meget naturligt, at kaninen kunne tale. - Men da den også tog et ur op af vestelommen, kiggede på det og skyndte sig af sted, sprang Alice op, for nu slog det hende, at hun aldrig nogen sinde havde set en kanin, der både havde vest på og et ur, den kunne tage op af lommen. Alice blev vældig nysgerrig og løb bag efter kaninen, tværs over marken. Hun nåede lige netop at se den smutte ned i et stort hul, der var under hækken. '''

Encrypted message:
Hkyr vot vyg åodwne Sviuo ai åivne hkmbon bod hisiorwx dwønwne kod hiec - bdwx ai rako ndqei kt ikgw åiy aia! Ot ekr yknyo hscdw ruc uiyqei s dwx bdq, sqåtwøec cag s fpød bod sa lpåe, bon vor kkr æxgwx bævlwneg s dwx oy reaveg snyon hkmiklwø ...  "Oy rvsn fdønqteaåe zkr bkn sp ec loy bdwx bævlwneg, yg zcog zegåocorco iåue hxaåueg wev ricknvon?" ihnåae Sviuo.  Msx kjxnw to ysvw åiy aia kt tsnvo kgknho, mwx vsø dwa sr wogåoba, ai nei cag bmsqec cægn ai øeøåe hsg dz oy zljukw leavih? Wecå Aascw ååaodwå ssn oy aæcutw prww oy aialayo (sr qova hjx kjxnw zå yøucn ax cagwec, neg qjdødw recne hvøk yg hivcsg) - dzdsqevo hjx pabdholæq ec rvæn ksxic wev øøvo øøxe. Von aib asgw pogli zonvo ...  Dwa vsø iåue hhrasg bhråcægniya, oy Klæme hfnios zolaor æukw, nei cag åægviy yvwørsåkwxdw, kt åknæxec åayne isl hsg holk: "Sh, vb gakdw cegnec! Tey uobweg pog åeca - Ds ruc aæcutw zå vot tkgwptwø, snxtwå Sæne 2 sp 57 hjx gsxsåo væåt, sa hjx bjødw cægo baovwa fdøbscswa, mwx læqe æ ijwllæukwa bwarsqtwne zbn vot hym cygwa mwqei xaibrasgi, kt åknæxec uucxe iklw. - Wec na von dqsr aoy ot jø oe kf kosioldwmwx, kæqgwne ej dwa oy åknxdio sæq ax åtwn, seøacq Aascw yp, xyr cb sayg vot zonvo, ai ruc klvøiy xoyon hsnvo hscdw åei on åknæx, dwø brne zkvvo vwåt ej oy ot jø, dwx kjxnw aayo oe kf aymbon. Sviuo baov khlvsg cfsyorgsg dq lql bsq exaeg uacsnwx, tkhrh yvwø msøkwx. Hjx nrodw viyo nwaoe kt ho dwx sbbtio nwn i wa siyri rua, neg cag bnvor zhkåon. 

 Translated text in 3 substrings for frequency analysis
HRTGDEIAIEMNDSRDNEDEDAANETGIITRNHDUIEDBSTEAFDDLENRRGBLEDOEENNMLOVFNEERNEODBLEGOEORIEAEEINNNEIMKNOVIITNKNMVDSOOAEAMEÆAEEGOLKEIEACÅDSOÆTROIASOHKNÅUAAEEJDEEØGVGDEHPDLEVKIEØØENBGOINDVIERGRÆIOLENSLRKEAÆIVRKDTNEAELGLHGDEEEOEOEDUÆTÅTGTSTSEHGSVTHBDÆBVFBSMLEJLKBRTENTMGMEARGTNEUELEANSOTOFSLMKGEDOKDSATSAACPRSGTNAULIONNHDENNDBEVVTOTDKNAOFMNIBVLGSRGLBEEANTRVMKHNDINOTDSTNISRUEANRKN
Counter({'E': 57, 'N': 36, 'D': 28, 'A': 23, 'O': 23, 'T': 23, 'I': 21, 'G': 19, 'R': 19, 'S': 18, 'L': 17, 'K': 13, 'V': 13, '\xc3': 12, 'B': 11, 'M': 11, 'H': 9, '\x86': 6, 'U': 6, 'F': 5, '\x85': 3, '\x98': 3, 'C': 2, 'J': 2, 'P': 2})
KVVÅWSUIVHBBHIWWWKHCWIKDIIWYAEYYSWCYIWDQWCGPBSPBVKÆWÆWGWYAGYHIWYSDQAZBSCYWÆWGZGGCCÅHÅGVCVIÅSUSJWYWYATVGHWSWRGBIIGSCGIØHDYJWAHCAWAWSYCWWYAYRVJJWYCXGCGDWCHKHCDSVJAHÆCÆSCVVØVAAWGZVWSÅHABÅGYYÆHIZAÆWIGGYWSWWÅÆCYIHHKVAWGCYBGGCSCCWVTWWNWÆSJSÅÆSJJWGAWDSWWÆÆWÆWWSWZVHCWWIIAIÅÆCCIWCVDRYJEKIDWÆWEWYNIÆXWECAWXCAVZVICVYYHVSWIÅÆWRZVWEYJWJWYEABSUAKVCYGDQSXGCWKHWSWJRWYWEHWBIWWIIAGGVZÅ
Counter({'W': 66, 'C': 30, '\xc3': 30, 'Y': 28, 'G': 25, 'I': 25, 'S': 24, 'V': 24, 'A': 21, 'H': 19, '\x86': 17, 'J': 12, '\x85': 11, 'B': 10, 'D': 10, 'K': 9, 'Z': 8, 'E': 7, 'R': 5, 'X': 4, 'Q': 3, 'U': 3, '\x98': 2, 'N': 2, 'P': 2, 'T': 2})
YOYONVOÅNKOOIOXØNOIBXROQKKÅAOKKOCRUQSXQÅØCSØOAÅOOKXXVNSXRVSOKKØRNØTÅKKPLBXVNYCZÅOOUXUWRKOHAVOXXTSÅAKSOKOXØAWÅANCBQCNØÅSZZULVWÅSÅOÅNAUPWALOQAXXZØNCWNQØRNVYISZQOXBOQRNXWØOXOISPLOOAØUHSHCNAKMFOOOUNCÅVYØÅXKKXÅNSSOSBKCNTUWPÅARAUZOKPØXÅNPXXOÅAXØCOOAØCAXQILUAAQNBOYYAQXBSKKXUXKWNOQAOØKOOWXQNJAÅXOQÅNØQSYYBYOOORKØXOSOCÅOKXØNKOÅJOØXXAOKYOVOOHSFOSQLQAUSXHYØØXXOVOAKOXBONAYRNCBOHO
Counter({'O': 61, '\xc3': 44, 'X': 36, 'K': 27, 'A': 25, 'N': 25, '\x85': 22, '\x98': 22, 'S': 20, 'Q': 17, 'C': 13, 'Y': 13, 'U': 12, 'B': 10, 'R': 10, 'V': 10, 'W': 9, 'H': 6, 'L': 6, 'P': 6, 'Z': 6, 'I': 5, 'T': 3, 'F': 2, 'J': 2, 'M': 1})
