import socket,random

#-----------------Constantes-------------------
words = [
  "sobre","año","todos","tiempo","vida","gobierno","siempre","día","país","mundo","año","estado","forma","general","presidente","mayor","momento","millón","hoy","lugar","trabajo","política","pasado","poder","partido","persona","grupo","cuenta","mujer","fin","ciudad","social","sistema","historia","punto","noche","agua","parece","situación","ejemplo","acuerdo","estado","tarde","ley","guerra","proceso","realidad","sentido","lado","cambio","número","sociedad","centro","padre","gente","final","relación","cuerpo","obra","madre","problema","hombre","información","ojos","muerte","nombre","público","siglo","mañana","derecho","verdad","cabeza","equipo","director","nivel","familia","ministro","seguridad","semana","proyecto","mercado","programa","palabras","internacional","empresa","libro","dios","fuerza","acción","amor","policía","puerta","zona","interior","música","campo","presencia","dinero","comisión","servicio","producción","papel","especial","capital","libertad","espacio","población","principio","cultura","arte","paz","sector","imagen","personal","interés","movimiento","actividad","difícil","joven","futuro","posibilidad","educación","atención","capacidad","investigación","figura","comunidad","necesidad","organización","calidad"
]
words = list(set(words)) #Elimina palabras repetidas
alphabet = "abcdefghijklmnñopqrstuvwxyzáéíóú"
UDP_IP = "localhost"
UDP_PORT = 8000

#-------------------------------------------------
#-----------------Funciones-----------------------
#Ordena conforme la longitud de la cadena
def lensort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if len(a[i]) < len(a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

#Obtiene las palabras al azar del arreglo de palabras
def getSoup(a):
  cant_pal= random.randint(14,16)
  i = 0
  soup = []
  n = len(a) - 1

  numbers = random.sample(range(0,n),cant_pal) #Para que las palabras se escojan al azar sin repetirse
  while i < cant_pal:
    soup.append(a[numbers[i]])
    i = i+1

  return lensort(soup)

#Rellena una cadena con un alfabeto 
def getRandomLetters(a,aux,m):
  i = 0
  n = len(a) - 1

  while i < m:
    aux = aux + a[random.randint(0,n)]
    i = i+1

  return aux

#Compara una palabra con sus posiciones contra el diccionario de palabras 
def compareWords(p,word,x,y,o):
  wLen = len(word)
  for wordss, positions in p.items():  
     
    for po in positions:
      i = 0
      while i < wLen :
        wAux = word[i]          
        #print("wAux: "+wAux+"\nchar:"+positions[po])
        if o == 0: #Hacia arriba
          if po[0] == x:
            if po[1] == y-i:
              if wAux != positions[po]:
                return False
        elif o == 1: #Hacia la esquina superior derecha
          if po[0] == x+i:
            if po[1] == y-i:
              if wAux != positions[po]:
                return False
        elif o == 2: #Hacia la derecha
          if po[0] == x+i:
            if po[1] == y:
              if wAux != positions[po]:
                return False
        elif o == 3: #Hacia la esquina inferior derecha
          if po[0] == x+i:
            if po[1] == y+i:
              if wAux != positions[po]:
                return False
        elif o == 4: #Hacia abajo
          if po[0] == x:
            if po[1] == y+i:
              if wAux != positions[po]:
                return False
        elif o == 5: #Hacia la esquina inferior izquierda
          if po[0] == x-i:
            if po[1] == y+i:
              if wAux != positions[po]:
                return False
        elif o == 6: #Hacia la izquierda
          if po[0] == x-i:
            if po[1] == y:
              if wAux != positions[po]:
                return False
        elif o == 7: #Hacia la esquina superior izquierda
          if po[0] == x-i:
            if po[1] == y-i:
              if wAux != positions[po]:
                return False
        i = i+1

  return True

def getPositions(w,positions,xw,yw):
  i = 0
  validate = 0
  wlen = len(w)

  while i < wlen:
    o = random.randint(0,7) #Orientacion
    wi = w[i]
    wiLen = len(wi)
    j = 0
    do_while = True
    count = 0
    positions[wi]={}
    
    if o == 0: #Hacia arriba
      while do_while:
        x = random.randint(0,xw)
        y = random.randint(wiLen-1,yw)

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 1
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 9
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x,y-j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(0,8) : m , (0,7): a , (0,6): l}
        j = j+1


    elif o == 1: #Hacia la esquina superior derecha
      while do_while:
        x = random.randint(0,xw-(wiLen-1))
        y = random.randint(wiLen-1,yw)

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 2
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 10
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x+j,y-j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(0,8) : m , (1,7): a , (2,6): l}
        j = j+1


    elif o == 2: #Hacia la derecha
      while do_while:
        x = random.randint(0,xw-(wiLen-1))
        y = random.randint(0,yw)

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 3
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 11
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x+j,y)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(0,8) : m , (1,8): a , (2,8): l}
        j = j+1

    elif o == 3: #Hacia la esquina inferior derecha
      while do_while:
        x = random.randint(0,xw-(wiLen-1))
        y = random.randint(0,yw-(wiLen-1))

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 4
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 12
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x+j,y+j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(0,8) : m , (1,9): a , (2,10): l}
        j = j+1

    elif o == 4: #Hacia abajo
      while do_while:
        x = random.randint(0,xw)
        y = random.randint(0,yw-(wiLen-1))

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 5
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 13
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x,y+j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(0,8) : m , (0,9): a , (0,10): l}
        j = j+1

    elif o == 5: #Hacia la esquina inferior izquierda
      while do_while:
        x = random.randint(wiLen-1,xw)
        y = random.randint(0,yw-(wiLen-1))

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 6
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 14
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x-j,y+j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(2,8) : m , (1,9): a , (0,10): l}
        j = j+1

    elif o == 6: #Hacia la izquierda
      while do_while:
        x = random.randint(wiLen-1,xw)
        y = random.randint(0,yw)

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 7
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 15
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x-j,y)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(2,8) : m , (1,8): a , (0,8): l}
        j = j+1

    elif o == 7: #Hacia la esquina superior izquierda
      while do_while:
        x = random.randint(wiLen-1,xw)
        y = random.randint(wiLen-1,yw)

        #print('bucle')
        count = count + 1 

        if count > 80 and i == wlen-1:
          validate = 8
          do_while = False
        if count > 160 and i == wlen-2:
          validate = 16
          do_while = False
        if i != 0:
          do_while = not compareWords(positions,wi,x,y,o)
        else:
          do_while = False  
      
      while j < wiLen:
        tup = (x-j,y-j)
        positions[wi][tup] = wi[j] # Ejemplo. mal: {(2,8) : m , (1,7): a , (0,6): l}
        j = j+1

    i = i+1
  return validate,positions

def fillTable(table,p):

  for wordss, positions in p.items():  

    #print("Entro")
    for po in positions:
      tableYLen = len(table[po[1]])
      auxT = ''
      i=0

      while i < tableYLen :
        #print("po[0]= "+str(po[0])+"   i="+str(i)+"  po[1]= "+str(po[1]))
        if po[0] == i :
          auxT = auxT + positions[po]
        else:
          auxT = auxT + table[po[1]][i]
        i = i + 1
      #print(auxT)
      table[po[1]] = auxT

  return table

def wordSearch(p,x1,y1,x2,y2):
  #print("Entro")
  val = False
  longit = 0

  if abs(x1-x2) > abs(y1-y2) :
    longit = abs(x1-x2)+1
  else:
    longit = abs(y1-y2)+1

  for wordss, positions in p.items():
    #print("Entro1")
    wLen = len(wordss)  
    for po in positions:
      #print("Entro2")
      if po[0] == x1 or po[0] == x2:
        #print("Entro3")
        if po[1] == y1 or po[1] == y2:
          #print("Entro4")
          if val == False:
            #print("Entro5")
            val = True
          else:
            if wLen == longit:
              return True,wordss

  return False,''

def wordSearchA(p,x1,y1,x2,y2,a):
  val = False
  longit = 0

  if abs(x1-x2) > abs(y1-y2) :
    longit = abs(x1-x2)+1
  else:
    longit = abs(y1-y2)+1

  for wordss, positions in p.items():
    wLen = len(wordss)  
    for w, wp in a.items():
      if w != wordss:
        for po in positions:
          if po[0] == x1 or po[0] == x2:
            if po[1] == y1 or po[1] == y2:
              if val == False:
                val = True
              else:
                if wLen == longit:
                  return True,wordss

  return False,''
#---------------------------------------------

#-------------Socket Server Logic-------------
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    d = sock.recvfrom(1024)
    data = d[0]
    addr = d[1]
     
    if not data: 
        break
     
    word = data.decode('utf-8')
    print(word)
    tipo= random.randint(1,3)

    if word == '1':
      i=0
      tablero = []
      answers = {}
      while i < 15:
        aux = ''
        tablero.append(getRandomLetters(alphabet,aux,15))
        i = i+1
      sopa = getSoup(words)

      positions = {}
      v=0
      do_while = True

      xp=14
      yp=14
      while do_while:
        v,positions = getPositions(sopa,positions,xp,yp)

        if v == 0:
          do_while = False
        else:
          print("Entro a la redimension")
          if v == 1 or v == 9 or v == 5 or v == 13:
            xp = xp +2
            i = 0
            tLen = len(tablero)
            while i < tLen:
              tablero[i]=getRandomLetters(alphabet,tablero[i],len(tablero[i])+2)
              i = i+1

          elif v == 3 or v == 11 or v == 7 or v == 15:
            yp = yp +2
            aux=''
            tablero.append(getRandomLetters(alphabet,aux,len(tablero[0])))
            tablero.append(getRandomLetters(alphabet,aux,len(tablero[0])))

          else:
            xp = xp +1
            yp = yp +1
            i = 0
            tLen = len(tablero)
            while i < tLen:
              tablero[i]=getRandomLetters(alphabet,tablero[i],len(tablero[i])+1)
              i = i+1
            aux=''
            tablero.append(getRandomLetters(alphabet,aux,len(tablero[0])))

      tablero = fillTable(tablero,positions)
      print(positions)

      sock.sendto(str(len(tablero)).encode('utf-8') , addr)
      for t in tablero:
        sock.sendto(str(t).encode('utf-8') , addr)

      sock.sendto(str(len(sopa)).encode('utf-8') , addr)
      print('sopa: '+str(len(sopa)))
      sock.sendto(str(tipo).encode('utf-8') , addr)
      print('tipo: '+str(tipo))

      pistas = {}
      j = 0
      
      do_while2=True
      while do_while2:
        r = random.randint(0,len(sopa)-1)
        k = 0

        for s in sopa:
          val2 = False
          aux2 = ''

          for a,c in answers.items():
            if a == s:
              aux2 = a+": "+c
              val2 = True

          if val2 == True:
            sock.sendto(aux2.encode('utf-8') , addr)
          else:
            if tipo == 1:
              sock.sendto(str(s).encode('utf-8') , addr)
            elif tipo == 2:
              if j != 0:
                if r == k:
                  if pistas.get(s) == None:
                    pistas[s] = [0] 
                  else: 
                    pLen =len(pistas[s])
                    if pLen < len(s):
                      pistas[s].append(pLen)

              if pistas.get(s) != None:
                i = 0
                pLen = len(pistas[s])
                auxP = ''
                while i < pLen:
                  auxP = aux+str(s[pistas[s][i]])
                  i = i+1
                sock.sendto(auxP.encode('utf-8') , addr)
              else:
                sock.sendto(' '.encode('utf-8') , addr)
            else:
              sock.sendto(str(len(s)).encode('utf-8') , addr)
          k = k+1  

        d = sock.recvfrom(1024)
        x1 = int(d[0].decode('utf-8'))

        d = sock.recvfrom(1024)
        y1 = int(d[0].decode('utf-8'))

        d = sock.recvfrom(1024)
        x2 = int(d[0].decode('utf-8'))

        d = sock.recvfrom(1024)
        y2 = int(d[0].decode('utf-8'))
        print(str(x1)+'\n'+str(y1)+'\n'+str(x2)+'\n'+str(y2))

        val = False
        w = ''
        if len(answers) == 0:
          val,w=wordSearch(positions,x1,y1,x2,y2)
        else:
          val,w=wordSearchA(positions,x1,y1,x2,y2,answers)

        

        if val == True:
         
          ans="("+str(x1)+","+str(y1)+") a ("+str(x2)+","+str(y2)+")"
          answers[w]=ans
          
          if len(answers) == len(sopa):
            do_while2 = False
            sock.sendto(str(2).encode('utf-8') , addr)
          else:
            sock.sendto(str(1).encode('utf-8') , addr)
          sock.sendto((w+": "+ans).encode('utf-8') , addr)
        else:
          sock.sendto(str(0).encode('utf-8') , addr)
          sock.sendto("No se encuentra ninguna palabra entre las coordenadas indicadas.\nPruebe de nuevo.".encode('utf-8') , addr)
        
        d = sock.recvfrom(1024)
        salir = int(d[0].decode('utf-8'))

        if salir == 2:
          break
        j = j+1

        
    #elif word == '2':

    elif word == '3':
      break

    else:
      reply = '\nNo envió un número correcto. Pruebe de nuevo.'
      sock.sendto(reply.encode('utf-8') , addr)

    
    print ('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.decode('utf-8'))

#---------------------------------------------
    

    


