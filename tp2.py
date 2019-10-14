# author : Thibaut Branlant 
# TP 2 : Codage Huffman
# Entrez le texte que vous voulez coder dans le fichier text.txt 
# Exectuter le fichier tp2.py et tout les informations concernant 
# la phrase coder et decoder ce trouveras dans le fichier 
# text_sorti.txt

from operator import itemgetter, attrgetter
import heapq
class TNode:
    # constructor
    def __init__(self,data,frequence, leftChild = None, rightChild = None):
        self._data = data
        self._frequence = frequence
        self._leftChild = leftChild
        self._rightChild = rightChild
    # get/set
        
    @property
    def data(self): return self._data
    @data.setter
    def data(self,data): self._data = data
    @property
    def frequence(self): return self._frequence
    @frequence.setter
    def frequence(self,frequence): self._frequence = frequence
    @property
    def leftChild(self): return self._leftChild
    @leftChild.setter
    def leftChild(self,ref): self._leftChild = ref
    @property
    def rightChild(self): return self._rightChild
    @rightChild.setter
    def rightChild(self,ref): self._rightChild = ref
    def __lt__(self,other): return self.frequence < other.frequence

    def __repr__(self) : 
        return "data :({}), freq({}), leftC({}), rightC({})  \n".format(
        self.data, self.frequence, self.leftChild, self.rightChild)

    def __eq__(self, other):
        if not other:
            return False
        else:
             
            return self.data == other.data and self.frequence == other.frequence and self.leftChild == other.leftChild and self.rightChild == other.rightChild

def remplissage_arbre(arbre_traitement) :
    while len(arbre_traitement) != 1 :
        node_tempo_1 = heapq.heappop(arbre_traitement)
        node_tempo_2 = heapq.heappop(arbre_traitement)
        node = TNode( '.',(node_tempo_1.frequence+node_tempo_2.frequence), node_tempo_1,node_tempo_2 )
        heapq.heappush(arbre_traitement,node)
    return(node)

def remplissage_hashage(arbre_root,code,hashtable) :
    if ( arbre_root.leftChild == None and arbre_root.rightChild == None):
        hashtable.update({arbre_root.data:code})
        return hashtable
    remplissage_hashage(arbre_root.leftChild,code + '0',hashtable) 
    remplissage_hashage(arbre_root.rightChild,code + '1',hashtable) 

def affichage_codage_huffman() :
    coder = ''
    for i in range (len(phrase)) :
        coder += hashtable.get(phrase[i])   
    return(coder)
    
def decodage_huffman(coder,arbre_root,i,phrase_fini,phrase) :
    
    if len(phrase) == len(phrase_fini) : 
       return phrase_fini
    if arbre_root.leftChild != None and arbre_root.rightChild != None :
        if coder[i] in '0':
            i += 1
            return decodage_huffman(coder,arbre_root.leftChild,i,phrase_fini,phrase)
        else :      
            i += 1
            return decodage_huffman(coder,arbre_root.rightChild,i,phrase_fini,phrase)
            
    else :
        lettre = arbre_root.data
        phrase_fini = phrase_fini + lettre
        arbre_root = arbre_save
        return decodage_huffman(coder,arbre_root,i,phrase_fini,phrase)

#ON OPEN UN FICHIER TXT     
f1 = open("text.txt","r")
phrase = f1.read()
#REMPLISSAGE DES PREMIERES NODES 
table = []
grande_table = []
for i in range (len(phrase)) :
    t1 = phrase[i]
    t2 = phrase.count(phrase[i])
    node_primaire = TNode(t1,t2)
    if TNode(node_primaire.data ,node_primaire.frequence) not in grande_table:
        grande_table.append(node_primaire)  
#FIN DE REMPLISSAGE DES PREMIERES NODES 

arbre_traitement = grande_table
#CREATION DE HEAPQ 
heapq.heapify(arbre_traitement)
#VARIABLES UTILES POUR LE CODAGE  
arbre_root = remplissage_arbre(arbre_traitement)
hashtable = {}
code = ''
remplissage_hashage(arbre_root,code,hashtable)
print(arbre_root)
print(hashtable)
#FIN CODAGE
#VARIABLE UTILE POUR LE DECODAGE 
phrase_fini = ''
arbre_save = arbre_root
affichage_codage_huffman()
coder = affichage_codage_huffman()
print(coder)

for i in range (len(coder)) :
    if len(phrase_fini) != len(phrase) : 
        phrase_fini = decodage_huffman(coder,arbre_root,i,phrase_fini,phrase)

print(phrase_fini)
# FIN DECODAGE

#OUVERTURE ET ECRITURE DU FICHIER DE SORTI
f2 = open("text_sorti.txt","w")
fin = "\n CODAGE : "+coder+" \n PHRASE DE BASE : " + phrase + "\n PHRASE FINI : " + phrase_fini
f2.write(str(fin))
        
        




