# fsm_sindarin

## README
This project is a simple transducer for the fictional language Sindarin developed by Tolkien. Because the language is only partially documented, a full model of the language is _not_ the goal; however, it was chosen because of two features:

* vocal shifts to build plurals
* mutations of consonants at the beginning of words

The focus of this project lies in the modeling of these two features. The capability of the file is demonstrated with three Sindarin texts which were written by Tolkien himself (in the folder 'texts'), as well as a test.txt file. They are short, but the longest texts written in Sindarin; and suited for the small scale of this project.

## STRUCTURE OF PROJECT
The main part of this project is the sindarin.xfst, which loads word lists and implements the transducer. In the folder words you find the python script used to generate word lists.

## USAGE & REQUIREMENTS
Use sindarin.xfst with XFST as usual. The python script for words is written for python 3; besides that, no special requirements exist.

## STATUS OF PROJECT
Due to the fact that word list acquisition was a lot more complicated than expected, and because Plural vowel shifts are a lot more complicated than expected, there was no time to fully explore how to best deal with mutations. There's some code that sketches how mutations can be dealt with, but unfortunately there wasn't enough time.

The strategy proposed is very much in a concatenative linguistics mindset, and because of this, has the limitations of being based on words, rather than sequences of words. The advantage of this is that it allows for independent generation of words; and is not concerned with the special cases that _cause_ the mutations, but just the different forms a word can have. To some degree, it is also a matter of interpretation when two mutations for different reasons occur, which is the reason one settles for. (For example, in the case of the mixed mutation).

Furthermore, there's some more complicated rules in the Plural vowel shifts that only affect very few words, but are very difficult to implement. However, for the sake of completeness, they should be implemented.

## ZEITAUFWAND / ZEITPLANUNG
* git lernen + einrichten: 2h
	* [Git Hub Tutorial][git tutorial]
	* [Markdown Tutorial][md tutorial]	
* Readme-Ziel schreiben + putzen: 1h
* Sindarin
	* Texte beschaffen + säubern ([Tolkien Gateway][tg]) (0.5h)
	* Wortliste von [Hisweloke][hisweloke]. Da die aktuelle Version des Lexikons nur als HTML verfügbar ist, musste diese geparst werden. Aufgrund verschiedener Probleme, die in words/notes.txt beschrieben sind, hat das viel länger als erwartet gedauert (7h)
* Pt 1: Plural-Bildung 
	* Erwies sich als deutlich komplizierter als erwartet (7h)
* Code säubern + dokumentieren: 1h

## RESOURCES
* [Grammar for Plurals][sindarin plurals]
* [Hisweloke Word Lists][hisweloke]
* [Wikipedia on Sindarin][wiki sin]

[git tutorial]: https://try.github.io
[md tutorial]: http://daringfireball.net/projects/markdown/basics
[tg]: http://tolkiengateway.net/wiki/King's_Letter
[hisweloke]: http://www.jrrvf.com/hisweloke/sindar/online/english.html
[sindarin plurals]: http://sindarin.de/grammatik.shtml#plural
[wiki sin]: https://en.wikipedia.org/wiki/Sindarin#Consonants
