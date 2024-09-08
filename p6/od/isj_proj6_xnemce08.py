#!/usr/bin/env python3

class Polynomial():
    def __init__(self, *polynom, **kwargs):              #transformuje argument pri vytvarani triedy na standardnu formu polynomu
        self.polynome = []                               #triedna premenna drziaca standardnu formu polynomu
        if len(polynom) == 0:               #spracovanie keyword argumentov
            indexes = {}
            for key in kwargs.keys():       #vytvori sa slovnik kde su kluce bez 'x', aby sa s hodnotami dalo pracovat ako s cislami
                indexes[key[1:]] = kwargs[key]

            maxIndex = int(max(indexes.keys()))

            for i in range(0, maxIndex + 1):                #postupne sa naplna self.polynome hodnotami z vytvoreneho slovnika
                if str(i) in indexes:
                    self.polynome.append(indexes[str(i)])
                else:
                    self.polynome.append(0)                 #prazdne miesta sa naplnia 0
        
        elif isinstance(polynom[0], list):         #spracovanie argumentu typu list
            self.polynome = polynom[0]
        else:                                       #spracovanie argumentu jednotlivych hodnot
            for arg in polynom:
                self.polynome.append(arg)
        
        i = len(self.polynome) - 1

        while(self.polynome[i] == 0 and i>0):       #v reprezentacii polynomu sa odstrania prebytocne nuly
            self.polynome.pop(i)
            i -= 1


    def __repr__(self):
        return self.printPoly()
    def __str__(self):
        return self.printPoly()
    
    def __eq__(self,other):
        return(self.polynome == other.polynome)
    
    def __add__(self, other):
        newPoly = []                #pomocna premenna kde sa uklada vysledok
        for i in range(0, min(len(self.polynome), len(other.polynome))):        #scitanie na indexoch pritomnych v oboch polynomoch
            newPoly.append(self.polynome[i] + other.polynome[i])
        if len(self.polynome) > len(other.polynome):                            #doplnenie ostatnych hodnot z vacsieho z polynomov
            for j in range(min(len(self.polynome), len(other.polynome)), max(len(self.polynome), len(other.polynome))):
                newPoly.append(self.polynome[j])
        elif len(self.polynome) < len(other.polynome):
            for j in range(min(len(self.polynome), len(other.polynome)), max(len(self.polynome), len(other.polynome))):
                newPoly.append(other.polynome[j])
        return Polynomial(newPoly)
    
    def __pow__(self, power):
        newPoly = self.polynome.copy()                                          #pomocna premmena kde sa uklada vysledok
        for i in range(0,power-1):
            tpoly = {}                                                          #dalsia pomocna premenna na medzivypocty                 
            for calculated in range(0, len(newPoly)):                           #iteruje sa cez vsetky hodnoty medzivysledku a povedneho polynomu (skalarny sucin)
                for original in range(0,len(self.polynome)):
                    index = (calculated + 1 * original + 1) - 1                 #vypocet novej mocniny pri x
                    value = (newPoly[calculated]) * self.polynome[original]     #vypocet hodnoty pri tejto mocnine
                    if index in tpoly:                                          #pridanie danej mocniny do medzivypoctu
                        tpoly[index] += value
                    else:
                        tpoly[index] = value
            newPoly = []
            for j in range(0, int(max(tpoly.keys())) + 1):                      #update medzivysledku medzivypoctom
                if j not in tpoly:
                    newPoly.append(0)       #niektore mocniny nemusia byt v medzivypocte, tam sa daju nuly
                else:
                    newPoly.append(tpoly[j])
        return Polynomial(newPoly)
            
    def printPoly(self):
        """
        Vypise polynom v standartnom formate
        """
        output=""                                       
        for i in reversed(range(0, len(self.polynome))):    #iteruje sa cez kazdy clen
            if(self.polynome[i] != 0):                      #nenulove cleny sa nevypisuju
                if(i != len(self.polynome)-1):              #ziskanie znaku znamienka
                    if(self.polynome[i] < 0):
                        operator = " - "
                    else:
                        operator = " + "
                else:
                    operator = ""
                
                if self.polynome[i] != 1 and self.polynome[i] != -1:               #ziskanie znaku clenu pri x
                    if(i != len(self.polynome)-1):                                 #najvyssi clen si nechava znamienko
                        if(self.polynome[i] > 0):
                            clen = str(self.polynome[i])
                        else:
                            clen = str(self.polynome[i])[1:]
                    else:
                        clen = str(self.polynome[i])            #kladne cleny znamienko nemaju
                elif self.polynome[i] == 1:                     #cleny 1 a -1 su vynimky - zobrazuju sa iba na najnizsom clene
                    if i==0:
                        clen = "1"
                    else:
                        clen = ""
                else:
                    if i==0:
                        clen = "1"
                    elif i == len(self.polynome)-1:
                        clen = "-"
                    else:
                        clen = ""


                if i > 1:                                   #ziskanie znakov pre clen x a text za nim. ^1 a ^0 sa nezapisuje
                    after = "x^" + str(i) 
                elif i == 1:
                    after= "x"
                else:
                    after = ""

                output += operator + clen + after    
        if output == "":           #ak nebolo nic pridane na vystup, polynom ma hodnotu 0
            output = "0"
        return output
    
    def derivative(self):
        """
        Vypise hodnotu derivacie polynomu
        """
        newPoly = []                                #premenna pre vysledok
        for i in range(1, len(self.polynome)):      #tym ze sa zacne od druheho prvku sa znizi rad polynomu
            newPoly.append(i * self.polynome[i])        
        
        if newPoly == []:                           #osetrenie prazdneho retazca ak bol povodny rad 1
            newPoly.append(0)
        return Polynomial(newPoly)
            
    def at_value(self, x, y=None):
        """
        Vypise hodnotu polynomu pre zadane x. Ak je zadane aj y tak vypise rozdiel medzi hodnotou polynomu pre y a hodnotou polynomu pre x
        """
        res = 0                         #hodnota pre zadane x
        for i in range(0, len(self.polynome)):
            res += self.polynome[i] * (x ** i)
        
        if y is not None:               #ak y bolo zadane, vytvori novu hodnotu pre medzivysledok a vrati rozdiel medzi hodnotami polynomu
            res2 = 0    
            for i in range(0, len(self.polynome)):
                res2 += self.polynome[i] * (y ** i)
            
            return res2 - res
        
        return res



def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()