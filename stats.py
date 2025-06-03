def get_num_words(i):
    with open(i) as f:
        file_contents = f.read()
        conteo = len(file_contents.split())
        return conteo

def get_num_letras(j):
    lista_conteo_letras = {}
    with open(j) as f:
        documento = f.read()
        for letra in documento:
            letra_m = letra.lower()
            if letra_m in lista_conteo_letras:
                lista_conteo_letras[letra_m] = lista_conteo_letras[letra_m] + 1

            else:
                lista_conteo_letras[letra_m] = 1
    return lista_conteo_letras

def sort_on(d):
    return d["num"]

def lista_solo_letras(x):
    lista_r = {}
    lista_c = get_num_letras(x)
    for b in lista_c:
        if b.isalpha():
            lista_r[b] = lista_c[b]
    return lista_r

def lista_ordenada(h):
    lista_r = lista_solo_letras(h)
    lista_o = []
    for e in lista_r:
        lista_o.append({"nom": e, "num": lista_r[e]})
    lista_o.sort(reverse=True, key=sort_on)
        #max_num = float("-inf")
        #letra_e = None
        #for i in lista_r:
            #if lista_r[i] > lista_r[e]:
                #max_num = lista_r[i]
                #letra_e = i
            #elif lista_r[i] == lista_r[e]:
                #max_num = lista_r[e]
            #elif 
    #lista_or = lista_solo_letras(h)
    
    return lista_o


def main():

    book_1 = get_num_words("books/frankenstein.txt")
    text_impresion = f"{book_1} words found in the document"
    print(text_impresion)
