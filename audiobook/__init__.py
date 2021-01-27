#!/usr/bin/python

import pyttsx3
import PyPDF2


class AudioBook:
    def __init__(self, book_path,spage):
        self.book_path = book_path
        self.start_page = int(spage)

    def text_to_speech(self):
        with open(self.book_path, "rb") as book:
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print("The Book has total: " + str(pages) + " pages!")

            # initiatiazing the pyttsx3 and setting voice speed to 125
            engine = pyttsx3.init()
            engine.setProperty("rate", 125)

            for num in range(self.start_page, pages):
                print("Reading page number " + str(num) + " page!")
                page = pdfReader.getPage(num)
                text = page.extractText()
                engine.save_to_file(text, "{}.wav".format(str(num))
