from __future__ import print_function
import functools
import random
import argparse

def clamp(lo, x, hi):
    return max(lo, min(x, hi))

def zip_keys(word, n=2):
    # Zip a tuple of the each set of <n> consecutive letters with the letter after that
    return zip(zip(*[word[i:] for i in range(n)]), word[n:])

class Markov(object):
    def __init__(self, corpus_filename, similarity=2):
        self.corpus_filename = corpus_filename

        self.minlen = 3
        self.maxlen = 13
        self.mu    = 6.70
        self.sigma = 1.60

        self.tuples = {}
        self.inits = set()

        with open(corpus_filename, 'r') as corpus_file:
            for word in corpus_file.read().splitlines():
                word = word.lower()
                for i, (key, letter) in enumerate(zip_keys(word, similarity)):
                    self.tuples.update( [(key, self.tuples.get(key, []) + [letter])] )
                    if i == 0:
                        self.inits.add(key)

        self.inits = list(self.inits)

    def generate(self, init_random=False):
        # Pokemon name lengths are between 3 and 12 characters
        # init_random=False: initialize from the start of an existing pokemon
        # init_random=True:  initialize randomly
        length = random.gauss(self.mu, self.sigma)
        length = int(clamp(self.minlen, length, self.maxlen))

        if init_random:
            key = random.choice(list(self.tuples.keys()))
        else:
            key = random.choice(self.inits)

        word = ''.join(key).lstrip()

        for i in range(length):
            if not key in self.tuples:
                break;
            character = random.choice(self.tuples.get(key))
            word += character
            key = key[1:] + (character,)

        return word

def main():
    parser = argparse.ArgumentParser(description='Generate new Pokemon names from an input file of known names.')
    parser.add_argument('filename', type=str,
                        help='input Pokemon name file, names separated by newlines')
    parser.add_argument('--num', metavar='N', type=int, default=1,
                        help='number of names to generate')
    parser.add_argument('--similarity', metavar='S', type=int, default=2,
                        help='similarity to input Pokemon names; 1 = gibberish, 2 = okay, >3 = very similar')
    parser.add_argument('--init-random', dest='init_random', action='store_const',
                        const=True, default=False,
                        help='initialize names randomly (default: initialize from the start of an existing Pokemon name)')

    args = parser.parse_args()

    m = Markov(args.filename, similarity=args.similarity)
    for i in range(args.num):
        print(m.generate(init_random=args.init_random))

if __name__ == "__main__":
    main()

