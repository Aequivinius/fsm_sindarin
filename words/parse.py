#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nico Colic

# Extracts dictionary entries from HTLM file
# Make sure to change source file in the ET.parse() below

import xml.etree.ElementTree as ET
import re
import time
import io

# The following is faster, because it allows to skip the XPath expression below. However, the code below is easier to understand
# word_type_pattern = re.compile('<small><i>(?P<type>[a-z]+\.|[a-z]\. and [a-z]+\.)</i></small>')

# starts with lowercase letter and ends in dot
word_type_regex = re.compile('[a-z]+.*\.')

word_types = dict()
nouns = list()
unwanted_lookalikes = [ 'pl.' , 'm.' , 'f.' , 'hypo.' , 'coll.']

tree = ET.parse('pruned_html.html')
root = tree.getroot()

start = time.time()
print('Parsing HTML now')

for child in root:
	word = child.get('id')
	
	# don't do any parsing on empty entries
	if word is "" or word is None:
		continue
	
	# pruning dictionary forms
	if word[-1:] is "-":
		word = word[:-1]
		
	if word[-2:-1] is ".":
		word = word[:-2]
	
	candidate_tags = child.findall('./small/i')
	
	for candidate in candidate_tags:
		if word_type_regex.match(candidate.text):
			
			# filter out information that looks like word types, but is not:
			if candidate.text not in unwanted_lookalikes:
				
				set_types = list()
				
				# check if word type is multiple (eg n. and adj.)
				# there is no word type that would contain 'and' itself
				# assuming that there are never more than two word types
				if 'and' in candidate.text:
					split_word_types = candidate.text.split()
					set_types.append(split_word_types[0][:-1])
					set_types.append(split_word_types[2][:-1])
				else:
					set_types = [candidate.text[:-1]]
				
				# set dictionary (cutting away final dot)
				word_type = candidate.text[:-1]
				if word in word_types:
					for set_type in set_types:
						word_types[word].append(set_type)
				else:
					word_types[word] = set_types
				
end = time.time()
print("Parsed HTML in ", end - start, " seconds")

# Writing to files and looking for nouns done in the same loop
# looping two times will give an AttributeError: 'list' object has no attribute 'items'
# which I don't know why
with io.open('word_types.txt','wt',encoding='utf-8') as f:
    for word, word_types in word_types.items():
	    for word_type in word_types:
		    if word_type is "n":
		    		nouns.append(word)
		    f.write(word + " : " + word_type + "\n")
print('Written dictionary to word_types.txt\n')

with io.open('nouns.txt','wt',encoding='utf-8') as n:
	for noun in nouns:
		n.write(noun + "\n")
print('Written nouns to nouns.txt')
