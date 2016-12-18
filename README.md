# vignere

* Vignere encoding modified from http://invpy.com/vigenereCipher.py 
* Extended to work with Danish letters
* Added code to do frequency analysis for decoded string with a period parameter
* 


usage: vignere.py [-h] (-e | -d) --text TEXT --key KEY [--period PERIOD]

Vignere Cipher with Danish Alphabet

optional arguments:
  -h, --help       show this help message and exit
  -e, --encrypt    use to encrypt a text
  -d, --decrypt    use to decrypt a text
  --text TEXT      text to encrypt or decript
  --key KEY        key to encrypt with
  --period PERIOD  take input text and split in "period" strings

EXAMPLE

./vignere.py -e --key FAR  --text '''Hvor det dog kedede Alice at sidde sammen med søsteren dernede ved søen - uden at have noget at tage sig til! Et par gange havde hun kigget i den bog, søsteren var i færd med at læse, men der var ingen billeder i den og heller ingen samtaler ...  "Og hvad fornøjelse har man af en bog uden billeder, og hvor personerne ikke snakker med hinanden?" tænkte Alice.  Man kunne jo give sig til at binde kranse, men var det så morsomt, at det var umagen værd at rejse sig op og plukke bellis? Mens Alice således sad og tænkte frem og tilbage (så godt hun kunne på grund af varmen, der gjorde hende sløv og søvnig) - opdagede hun pludselig en hvid kanin med røde øjne. Den løb lige forbi hende ...  Det var ikke særlig mærkværdigt, og Alice syntes heller ikke, det var særlig overraskende, at kaninen sagde til sig selv: "Ih, du glade verden! Jeg kommer for sent - Da hun tænkte på det bagefter, syntes Side 2 af 57 hun ganske vist, at hun burde være blevet forbavset, men lige i øjeblikket betragtede hun det som noget meget naturligt, at kaninen kunne tale. - Men da den også tog et ur op af vestelommen, kiggede på det og skyndte sig af sted, sprang Alice op, for nu slog det hende, at hun aldrig nogen sinde havde set en kanin, der både havde vest på og et ur, den kunne tage op af lommen. Alice blev vældig nysgerrig og løb bag efter kaninen, tværs over marken. Hun nåede lige netop at se den smutte ned i et stort hul, der var under hækken. ''' 


Encrypted message:
Mvcw dvy dcl kvieuj Aåncv ft gnduj srrmvs mvi spxtvweb iefseuj vvi spjn - iieb ft yfvv soxjt ry trle gng hnl! Vy prw grsgv majie yzn øngxjt z ieb gox, xøgyefjn jfr z kæfi mvi ah qægj, mvs dvw vrw ibleb giåqeujr z ieb tg yjlåjr zsgvs srrtrqef ...  "Tg yæau kofsøæjlgj hrw mrs aw jn stg iieb giåqeujr, cl hjtr djrgtnvwnv nkøj sbfkøjr ajd ynnrsdvs?" toskhj Aåncv.  Rab pubse æt gzæe gng hnl ry bzsdv prrssv, reb æaf ieh xå atrgtmh, ft ujt jfr iraxjn jcru ft fjjgj szl od tg dquøpe sjlåns? Ajng Flzhe gelvieg xau tg hcnøye wwea tg hnlsfgv (xå xtdh mub pubse de gfznu ff jfrajn, ujr xoofie yjnuj sådv cl spænzl) - odiaxjdv mub uliisvqix jn yæiu pabnn ajd fddv djbj. Dvs lpg lzle wtrsn hvsdv ...  Ieh æaf nkøj sowlzl mowkjcrungh, tg Rqitj smstvx hvqlvw iøpe, ujt jfr gcrång cæefwagpebie, ry krsibjn gfguj tzq szl svqv: "Zm, di llrie jjrujn! Æjg øtmajr wtr gjnh - Ia yzn hcnøye de dvy brlewyef, xybyeg Xiuj 2 aw 57 mub labxkv æigy, ah mub gufie jcrv glvæeh kofgajxeh, reb qixj i poesqiøpeh gehwaxyeuj his dvy scr ncleh rexjt bftiwlzlt, ry krsibjn øznbj trqe. - Ajn uf dvs oxxå htg vy uf tp rk vvxtvqoareb, pixleuj pq ieh tg gpybitv xix ff gyeu, xpffnx Flzhe cu, fcw ni xlcl dvy hvsdv, ft yzn rqdfng btgvs szsdv majie gjt vs krsib, ief gåuj hrædv æegy pq tg vy uf, ieb pubse hfgv tp rk lcrmvs. Aåncv glvæ voqdzl nmxgvwrzl ox qøs gax jfhjr øfnzseb, yvows cæef rafpeb. Mub såvie ångv sehtp ry sv ieb xmiytv seu n eh xtcwt yzl, ujr jfr isdvw hopkvs. 

 Translated text in 3 substrings for frequency analysis
MWYLIJNFNJRSIXWISJIJIFFSJYLNNYWSMIZNJIGXYJFKIIQJSWWLGQJITJJSSRQTÆKSJJWSJTIGQJLTJTWNJFJJNSSSJNRPSTÆNNYSPSRÆIXTTFJFRJCFJJLTQPJNJFHEIXTCYWTNFXTMPSEZFFJJOIJJDLÆLIJMUIQJÆPNJDDJSGLTNSIÆNJWLWCNTQJSXQWPJFCNÆWPIYSJFJQLQMLIJJJTJTJIZCYEYLYXYXJMLXÆYMGICGÆKGXRQJOQPGWYJSYRLRJFWLYSJZJQJFSXTYTKXQRPLJITPIXFYXFFHUWXLYSFZQNTSSMIJSSIGJÆÆYTYIPSFTKRSNGÆQLXWLQGJJFSYWÆRPMSINSTYIXYSNXWZJFSWPS
Counter({'J': 57, 'S': 36, 'I': 28, 'F': 23, 'T': 23, 'Y': 23, 'N': 21, 'L': 19, 'W': 19, 'X': 18, 'Q': 17, '\x86': 13, '\xc3': 13, 'P': 13, 'G': 11, 'R': 11, 'M': 9, 'C': 6, 'Z': 6, 'K': 5, 'E': 3, 'D': 3, 'H': 2, 'O': 2, 'U': 2})
VDDKEACTDSMMSTEEEVSNETVOTTEGLPGGAENGTEOØENRÆMAÆMDVIEIEREGLRGSTEGAOØLHMANGEIERHRRNNKSKRDNDTKACAUEGEGLBDRSEAEÅRMTTRANRTJSOGUELSNLELEAGNEEGLGÅDUUEGNFRNROENSVSNOADULSINIANDDJDLLERHDEAKSLMKRGGISTHLIETRRGEAEEKINGTSSVDLERNGMRRNANNEDBEEYEIAUAKIAUUERLEOAEEIIEIEEAEHDSNEETTLTKINNTENDOÅGUPVTOEIEPEGYTIFEPNLEFNLDHDTNDGGSDAETKIEÅHDEPGUEUEGPLMACLVDNGROØAFRNEVSEAEUÅEGEPSEMTEETTLRRDHK
Counter({'E': 66, 'N': 30, 'G': 28, 'R': 25, 'T': 25, 'A': 24, 'D': 24, 'L': 21, 'S': 19, 'I': 17, 'U': 12, 'K': 11, '\xc3': 10, 'M': 10, 'O': 10, 'V': 9, 'H': 8, 'P': 7, '\x85': 5, 'F': 4, '\x98': 3, 'C': 3, '\x86': 2, 'B': 2, 'J': 2, 'Y': 2})
CVCVUÅVGURVVPVBFUVPIBYVXRRGHVRRVJYØXZBXGFJZFVHGVVRBBÅUZBYÅZVRRFYUFÆGRRWSIBÅUCJDGVVØBØAYRVOHÅVBBÆZGHRZVRVBFHAGHUJIXJUFGZDDØSÅAGZGVGUHØWAHSVXHBBDFUJAUXFYUÅCPZDXVBIVXYUBAFVBVPZWSVVHFØOZOJUHRTMVVVØUJGÅCFGBRRBGUZZVZIRJUÆØAWGHYHØDVRWFBGUWBBVGHBFJVVHFJHBXPSØHHXUIVCCHXBIZRRBØBRAUVXHVFRVVABXUQHGBVXGUFXZCCICVVVYRFBVZVJGVRBFURVGQVFBBHVRCVÅVVOZMVZXSXHØZBOCFFBBVÅVHRVBIVUHCYUJIVOV
Counter({'V': 61, 'B': 36, 'R': 27, '\xc3': 25, 'H': 25, 'U': 25, 'G': 22, 'F': 22, 'Z': 20, 'X': 17, 'C': 13, 'J': 13, '\x98': 12, '\x85': 10, 'I': 10, 'Y': 10, 'A': 9, 'D': 6, 'O': 6, 'S': 6, 'W': 6, 'P': 5, '\x86': 3, 'M': 2, 'Q': 2, 'T': 1})
