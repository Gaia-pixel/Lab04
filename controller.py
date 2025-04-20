import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtInput, language, modality):
        txtInput = replaceChars(txtInput.lower())

        words = txtInput.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def handleSpellCheck(self, e):
        print("handle Spell Check called")

        sentence = self._view.txtIn.value
        if sentence == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Insert Sentence!"))
            self._view.update()
            return

        language = self._view.ddLanguage.value
        modality = self._view.ddModality.value

        if language == "Choose language":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Select Language!"))
            self._view.update()
            return

        if modality == "Choose modality":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text("Select Modality!"))
            self._view.update() # da mettere perchè se no non mi appare l'avviso sulla pagina
            return


        parole, elapsedTime = self.handleSentence(sentence, language, modality)

        self._view.txtOut.controls.clear()  # Svuoto il txtOut
        self._view.txtOut.controls.append(ft.Text("Sentence: " + sentence ))
        self._view.txtOut.controls.append(ft.Text("Wrong words: " + parole ))
        self._view.txtOut.controls.append(ft.Text("Time to check: " + str(elapsedTime) ))

        self._view.update()

    def handleLanguageSelection(self, e):
        print("handle Dropdown language called")
        self._view.txtOut.controls.append(ft.Text(value="Language correctly selected: " + self._view.ddLanguage.value))
        self._view.update()

    def handleModalitySelection(self, e):
        print("handle Dropdown modality called")
        self._view.txtOut.controls.append(ft.Text(value="Modality correctly selected: " + self._view.ddModality.value))
        self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text