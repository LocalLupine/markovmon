# markovmon

Generate Pokemon names (or anything really, given an input corpus of newline-separated names) using Markov chains.

Usage:

```bash
python markovmon.py -h
# usage: markovmon.py [-h] [--num N] [--similarity S] [--init-random] filename
# 
# Generate new Pokemon names from an input file of known names.
# 
# positional arguments:
#   filename        input Pokemon name file, names separated by newlines
# 
# optional arguments:
#   -h, --help      show this help message and exit
#   --num N         number of names to generate
#   --similarity S  similarity to input Pokemon names; 1 = gibberish, 2 = okay,
#                   >3 = very similar
#   --init-random   initialize names randomly (default: initialize from the
#                   start of an existing Pokemon name)

python markovmon.py data/pokemon_en.txt
# lybateel

python markovmon.py data/pokemon_en.txt --similarity=3 --init-random --num=5 
# inglery
# gedennekiddo
# acoong
# glybuffala
# isopod
```
