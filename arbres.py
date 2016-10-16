# -*- coding: utf8 -*-

def Property(func) :
    return property(**func())

class Arbre :
    """ Classe pour représenter des arbres """

    def __fromlist(self,liste) :
        """ Construit un arbre à partir de listes """
        assert(isinstance(liste, list) or isinstance(liste, tuple))
        assert(len(liste)>=1)
        if (isinstance(liste, list)):
            print('Creation a partir de liste')
        if (isinstance(liste, tuple)):
                print('Creation a partir de tuple')
        self.__noeud=liste[0]
        for sa in liste[1:] :
            self._fils.append(Arbre(sa))

    def __init__(self, first, **kwargs) :#label, listefils=None) :
        """
        Crée un arbre à partir
        1) d'un label et d'une liste de sous arbres éventuels
        2) Si le premier argument est une liste ou un tuple, il doit
           "bien construit" : en premier élément un label et en second
           élément une liste de fils suivant le même schéma.
        3) Un autre arbre (copie en profondeur)
        Exemple :
        a=Arbre('A',fils=[Arbre('B',Arbre('C')])
        b=Arbre(( 'A',(('B',('C')),'D') ))

        L'étiquette d'un noeud ne DOIT PAS être None
        """
        assert(first!=None)
        self.__noeud=None
        self._fils=[]
        if isinstance(first,list) or isinstance(first,tuple) :
            self.__fromlist(first)
        elif isinstance(first,Arbre) :
            self.__noeud=first.racine
            for sa in first._fils :
                if sa==None : self._fils.append(None)
                else : self._fils.append(Arbre(sa))
        else :
            self.__noeud=first
            self._fils=kwargs.get('fils',[])

    def __get_racine(self) :
        return self.__noeud
    def __set_racine(self, label) :
        self.__noeud=label
    racine=property(__get_racine,__set_racine,doc="Accède ou modifie le label de la racine")

    def ajoute(self,a) :
        """ Ajoute l'arbre a comme nouveau fils de la racine
        (en fin de liste)
        """
        assert(isinstance(a,Arbre))
        self._fils.append(a)

    def remplace(self,pos,a) :
        """ Remplace le fils de la racine situé en position pos par
        l'arbre a.
        """
        if pos<0 : pos=len(self._fils)-pos
        if pos<0 : raise IndexError('Position '+pos+' incorrecte')
        if pos>=len(self._fils) : raise IndexError('Position '+pos+' incorrecte')
        self._fils[pos]=a

    def hauteur(self):
        """ Renvoie la hauteur de l'arbre
            TODO
        """
        if self.getFils() == []:
            return 1
        else:
            listeOfHauteurs = []
            for fils in self.getFils():
                listeOfHauteurs.append(fils.hauteur())
            return 1 + max(listeOfHauteurs)

    def __iter__(self) :
        """ Itère sur les fils. Si un fils vaut 'None' il est ignoré """
        for l in self._fils :
            if l!= None :
                yield l
    def getFils(self) :
        return self._fils
    def __getitem__(self,i) :
        """ Renvoie une référence vers le fils numéro i
        Exemple :
        a=Arbre((4,5,(6,7,8)))
        b=a[1]
        print(b)
        >>> (6-(7,8))

        Lève IndexError si l'indice es incorrect
        """
        if i<0 : i<len(self._fils)-i
        if i not in range(len(self._fils)) :
            raise IndexError('Pas de fils '+str(i))
        return self._fils[i]

    def __setitem__(self,i,v) :
        """ Modifie le fils numéro i s'il existe et l'ajoute sinon
        """
        if i<0 : i<len(self._fils)-i
        if i<0 : raise IndexError('Pas de fils '+str(i))
        while len(self._fils)<=i : self._fils.append(None)
        if v.__class__==self.__class__ :
            self._fils[i]=v
        else :
            # Ci-dessous : à retenir, appelle Arbre(v) ou ArbreBinaire(v)
            # selon le type de self
            self._fils[i]=self.__class__(v)

    def __str__(self) :
        """ Renvoie une représentation lisible de l'objet sous
        forme de chaîne de caractères
        """
        s=[]
        for l in self._fils :
            if l==None : s.append('')
            else :s.append(str(l))
        s=",".join(s)
        if s!="" : return "("+str(self.__noeud)+"-("+s+"))"
        else : return str(self.__noeud)

    def __len__(self) :
        """ Renvoie le nombre de fils (différents de None) """
        return len([f for f in self._fils if f !=None])

    def __repr__(self) :
        if len(self._fils)==0 : return self.__class__.__name__+"("+repr(self.racine)+")"
        f=[]
        for l in self._fils :
            if l==None : f.append(repr(None))
            else :
                f.append(repr(l))
            pass
        return self.__class__.__name__+"(("+repr(self.racine)+","+",".join(f)+"))"

def hauteur(arbre):
    if arbre.getFils() == []:
        return 1
    else:
        listeOfHauteurs = []
        for fils in arbre.getFils():
            #print('Fils', fils)
            listeOfHauteurs.append(fils.hauteur())
        return 1 + max(listeOfHauteurs)


class ArbreBinaire(Arbre) :
    def __init__(self, first, **kwargs) :
        """
        Crée un arbre binaire à partir
        1) de la même façon qu'on crée un Arbre
        2) à partir d'un Arbre
        """
        if isinstance(first,Arbre) :
            l=[]
            for f in first._fils :
                if f==None : l.append(None)
                else : l.append(ArbreBinaire(f))
            Arbre.__init__(self,first.racine,fils=l[0:2])
        else :
            a=Arbre(first,**kwargs)
            self.__init__(a)

    def dot(self,printinfos=True) :
        """ Crée une chaîne de caractère contenant une
        description de l'arbre pour le programme dot (graphviz)
        Les fils sont ici ordonnés...
        """
        return 'digraph g {graph[ordering="out"];\n'+self._innerdot()+"}\n"

    @property
    def fg(self) :
        "Le fils gauche"
        return self._fils[0] if len(self._fils)>0  else None
    @fg.setter
    def fg(self,arb) :
        self.__setitem__(0,arb)

    @property
    def fd(self) :
        "Le fils droit"
        return self._fils[1] if len(self._fils)>0  else None
    @fd.setter
    def fd(self,arb) :
        self.__setitem__(1,arb)


    def _fg(self) :
        """ Référence vers le sous arbre gauche """
        return self._fils[0] if len(self._fils)>0  else None
    def _fd(self) :
        """ Référence vers le sous arbre droit """
        return self._fils[1] if len(self._fils)>1  else None
    def ajoute(self,a) :
        """ Ajoute l'arbre a comme nouveau fils de la racine
        (en fin de liste)
        """
        if len(self._fils)<2 : Arbre.ajoute(self,a)
        else : raise RuntimeError('Pas plus de deux fils pour un arbre binaire')

if __name__=='__main__' :
    ar=Arbre((10, 1, (4, 2, 5, 6, 7), 6, (13, (10, 5, 7), 11, 4), 15))
    ar2 = Arbre((10,1))
    # arbreFromListe = Arbre([0, 1, 2, 3])
    # print(arbreFromListe)
    # d=ArbreBinaire(4, fils=(ArbreBinaire(3),Arbre(7)))
    #print(isinstance(ar.getFils()[2], Arbre))
    #print(ar.getFils()[3].getFils())
    print(ar)
    print(ar.hauteur())
    #print(ar2)
    #print(ar2.getFils())
    print(hauteur(ar))


