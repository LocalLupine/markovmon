# markovmon

Generate Pokemon names (or anything really, given an input corpus of newline-separated names) using Markov chains.

Usage:

```bash
python markovmon.py -h
# usage: markovmon.py [-h] [--num NUM] [--similarity S] [--init-random] filename
# 
# Generate new Pokemon names from an input file of known names
# 
# positional arguments:
#   filename        Input Pokemon name file, names separated by newlines
# 
# optional arguments:
#   -h, --help      show this help message and exit
#   --num NUM       Number of names to generate
#   --similarity S  Similarity to input Pokemon names; 1 = gibberish, 2 = okay,
#                   >3 = very similar
#   --init-random   Initialize names randomly (default: initialize from the
#                   start of an existing Pokemon name)

python markovmon.py pokemon.txt
# lybateel

python markovmon.py --num=5 --similarity=3 --init-random pokemon.txt
# inglery
# gedennekiddo
# acoong
# glybuffala
# isopod
```
