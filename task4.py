#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

person = input("please enter a person's name.")
adjective = input("please enter a adjective")
food = input("please enter any food.")
noun = input("please enter a noun.")
place = input("please enter any place.")
verb = input("please enter a verb")
adverb = input("please enter an adverb")
thing = input ("please enter a thing.")

print(f"Today we picked apple from {person}'s Orchard. I had no idea there were so many different varieties of apples. I ate {adjective} apples straight off the tree that tasted like {food}. Then there was a {adjective} apple that looked like a {noun}.  When our bag was full, we went on a free hay ride to {place} and back. It ended at a hay pile where we got to {verb} {adverb}. I can hardly wait to get home and cook with the apples. We are going to make apple {food} and {thing} pies!")