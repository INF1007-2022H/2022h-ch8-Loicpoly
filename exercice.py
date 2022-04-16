#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import csv
import json
def exercice_1():
    with open('exemple.txt', 'r', encoding="utf-8") as f1, open('meteo.txt', 'r', encoding='Windows-1252') as f2:
        #If a file is created on windows, the default encodind to use is: 'Windows-1252'
        long1 = f1.read()
        long2 = f2.read()
        f1.seek(0)
        f2.seek(0)
        for i in range(min(len(long1), len(long2))):
            if f1.read(1) != f2.read(1):
                f1.seek(f1.tell() - 1)
                f2.seek(f2.tell() - 1)
                print(f"La première différence est apparue au caractère: {i+1} et il s'agit de: {f1.read(1)} et {f2.read(1)}")
                break
            else:
                continue

def exercice_2():
    with open('exemple.txt', 'r', encoding="utf-8") as f1, open('triple_space.txt', 'w', encoding="utf-8") as f2:
        for line in f1:
            for word in line.split():
                f2.write(f'{word}   ')
            f2.write(f'\n')

def exercice_3():
    with open('notes.txt', 'r', encoding="utf-8") as f1, open('notes_classees', 'w', encoding="utf-8") as f2:
        for note in f1:
            note = int(note)
            if note in range(80, 101):
                note_l = 'A'
            elif note in range(70, 80):
                note_l = 'B'
            elif note in range(57, 70):
                note_l = 'C'
            elif note in range(50, 57):
                note_l = 'D'
            elif note in range(35, 50):
                note_l = 'E'
            elif note in range(0, 35):
                note_l = 'F'
            f2.write(f'{note}, {note_l}\n')

def exercice_6():
    with open('exemple.txt', 'r', encoding="utf-8") as f1, open('copie_1sur2.txt', 'w', encoding="utf-8") as f2:
        i = 0
        for line in f1:
            if i%2==0:
                f2.write(f'{line}\n')
            i+=1

def exercice_5():
    with open('exemple.txt', 'r', encoding="utf-8") as f1:
        liste = []
        for line in f1:
            for word in line.split():
                if word.isdigit():
                    liste.append(int(word))
    liste.sort()
    return liste



# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice_1()
    exercice_2()
    exercice_3()
    exercice_6()
    print(exercice_5())
    pass
