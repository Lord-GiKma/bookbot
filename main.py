import sys
from stats import get_num_letras
from stats import get_num_words
from stats import lista_solo_letras
from stats import lista_ordenada

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    libro = sys.argv[1]
    
    #libro = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {libro}...")  
    print("----------- Word Count ----------")  
    book_1 = get_num_words(libro)
    text_impresion = f"Found {book_1} total words"
    print(text_impresion)
    lista_ord = lista_ordenada(libro)
    for k in lista_ord:
        print(f"{k['nom']}: {k['num']}")
    print("============= END ===============")
    
main()
