# Find Pairs

[![Hippocratic License HL3-FULL](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-FULL&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/full.html)

A simple python script to extract pairs of characters from a given text for use in literary social network analysis.

## Method
This script searches a specified text for occurrences of the phrase `Name1 and Name2` using a user-provided list of character names. It's dead simple, devoid of nuance, and its success mostly depends on the size of the text (it works much better with [_Lord of the Rings_](https://lukehillman.net/2011/06/social-network-analysis/) than with _Fight Club_).

## Usage

You'll need to provide:
* a UTF-8 encoded text file containing a list of characters to search for, one per line.
* a UTF-8 encoded book (or other text) you want to search

Call findpairs.py followed by your character file and your book file, in that order. Optionally, include an output filename as the final argument.

Using the example files provided in this repo, you might type:

````
python3 findpairs.py examples/characters.txt examples/moby-dick.txt moby-dick_relationships.csv
````

This would produce the output:
````
Stubb,Flask,8
Starbuck,Stubb,4
Peleg,Bildad,3
Ahab,Starbuck,2
Starbuck,Queequeg,1
Queequeg,Tashtego,1
Queequeg,Daggoo,1
Stubb,Tashtego,1
````
Additionally, a file called `moby-dick_relationships.csv` would be created.

You can then use NodeXL or the SNA tool of your choice to generate a network visualization.

## Disclaimers

For the love of Bob, don't use this for anything important!

## License

This project uses the [Hippocratic License, v3.0](https://firstdonoharm.dev). TL;DR, it's not *quite* open source, but as long as you're not violating human rights, working for a fossil fuel company or military, conducting mass surveillance for either a government or a corporation, etc (see license for full details), you can essentially treat it as open source.

Copyleft applies. Any derivative works must use this license.
