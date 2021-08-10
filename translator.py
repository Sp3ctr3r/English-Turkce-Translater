from googletrans import Translator
import time
import os
import httpcore
import sys

dic = {}

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def transl():    
    while True:
        try:
            print("Çevrilen kelimeleri görmek için 't', Çıkmak için 'q' tuşuna basın!")
            word_or_sentences = input("Çevirilecek kelime veya cümle girin : ")
            language = input("Hangi dile çevrilsin? [tr(default)/en vs] : ")

            if language == "":
                language = "tr"
            elif language == "en":
                language = "en"
            elif language == "t":
                print("\n")
                print("Çevrilmiş olan kelimeler : ",dic)
                print("\n")

                d = input("Devam etmek için 'c', Çıkmak için 'Enter' tuşuna basın!: ")

                if d == "c":
                    clear()
                    continue

                elif d == "":
                    sys.exit()

                else:
                    print("\nLütfen geçerli değer girin!")
                    time.sleep(2)
                    clear()
                    continue

            elif language == "q":
                sys.exit()

            else:
                print("\n")
                print("Lütfen geçerli değer girin!")
                print("\n")
                time.sleep(1)
                clear()
                continue

            translator = Translator()
            translated = translator.translate(word_or_sentences, dest=language)
            t = translated.text

            assignment = {word_or_sentences: t}
            dic.update(assignment)

            if word_or_sentences == "t":
                print("\n")
                print("Çevrilmiş olan kelimeler : ",dic)
                print("\n")
                c = input("Devam etmek için 'c', Çıkmak için 'Enter' tuşa basın : ")

                if c == "c":
                    clear()
                    continue

                elif c == "":
                    sys.exit()

                else:
                    print("\nLütfen geçerli bir değer girin!")
                    time.sleep(2)
                    clear()
                    continue

            elif word_or_sentences == "q":
                sys.exit()

            else:
                print("\n")
                print("Çevirildi : ", t)
                print("\n")
                print("Çevrilen kelimeler : ", dic)
                print("\n")

            keepGo = input("Devam etmek için 'Enter', Çıkmak için 'q', Dil değiştirmek için 'l' tuşuna basın! : ")
            keepGo = str(keepGo)

            if keepGo == "q":
                sys.exit()

            elif keepGo == "l":
                clear()
                break

            elif keepGo == "":
                clear()
                continue

            else:
                print("\nLütfen geçerli değer girin!")
                time.sleep(2)

            clear()

        except(httpcore._exceptions.ConnectError):
            print("internete Ulaşılınamadı!")
            time.sleep(2)
            continue

def transl2():    
    while True:
        try:
            print("Press 't' to see translated words, Press 'q' to exit!")
            word_or_sentences = input("Enter word or sentence to translate : ")
            language = input("Which language to translate [en(default)/tr vs] : ")

            if language == "":
                language = "en"
            elif language == "tr":
                language = "tr"
            elif language == "t":
                print("\n")
                print("Words that have been translated : ",dic)
                print("\n")

                d = input("Press 'c' to continue, Press 'Enter' to log out : ")

                if d == "c":
                    clear()
                    continue

                elif d == "":
                    sys.exit()

                else:
                    print("\nPlease enter valid value!")
                    time.sleep(2)
                    clear()
                    continue

            elif language == "q":
                sys.exit()

            else:
                print("\n")
                print("Please enter valid value!")
                print("\n")
                time.sleep(1)
                clear()
                continue

            translator = Translator()
            translated = translator.translate(word_or_sentences, dest=language)
            t = translated.text

            assignment = {word_or_sentences: t}
            dic.update(assignment)

            if word_or_sentences == "t":
                print("\n")
                print("Words that have been translated : ",dic)
                print("\n")
                c = input("Press 'c' to continue, Press 'Enter' to log out : ")

                if c == "c":
                    clear()
                    continue

                elif c == "":
                    sys.exit()

                else:
                    print("\nPlease enter valid value!")
                    time.sleep(2)
                    clear()
                    continue

            elif word_or_sentences == "q":
                break

            else:
                print("\n")
                print("Translated : ", t)
                print("\n")
                print("Words that have been translated : ", dic)
                print("\n")

            keepGo = input("Press 'Enter' to continue, Press 'q' to exit, Press 'l' to change language! : ")

            if keepGo == "q":
                sys.exit()

            elif keepGo == "l":
                clear()
                break

            elif keepGo == "":
                clear()
                continue

            else:
                print("\nPlease enter valid value!")
                time.sleep(2)

            clear()

        except(httpcore._exceptions.ConnectError):
            print("Internet not reachable!")
            time.sleep(2)
            continue

def chooseLanguage():
    while True:
        try:
            opt = """
1-> Türkçe  | Çıkmak için 'q' tuşuna basın!
2-> English | Press 'q' to exit 
"""
            print(opt)

            choose = input("1 / 2  : ")
            print("")

            if choose == "1":
                clear()
                transl()
            
            elif choose == "2":
                clear()
                transl2()

            elif choose == "q":
                sys.exit()

            elif choose == "":
                print("Please enter 1 or 2!")
                time.sleep(2)
                clear()

            else:
                print("Please enter 1 or 2!")
                time.sleep(2)
                clear()

        except ValueError:
            print("Please enter only number!")

chooseLanguage()