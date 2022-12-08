from collections import Counter
import random

sarki = """ A-well, a bird, bird, bird, bird is the word
A-well, a bird, bird, bird, well-a bird is the word
A-well, a bird, bird, bird, b-bird's the word
A-well, a bird, bird, bird, well-a bird is the word
A-well, a bird, bird, b-bird is the word
A-well, a bird, bird, bird, b-bird's the word
A-well, a bird, bird, bird, well-a bird is the word
A-well, a bird, bird, b-bird's the word
A-well-a don't you know about the bird?
Well, everybody knows that the bird is the word """

print(Counter(sarki))
print(Counter(sarki.lower().split()))#split kelimelere böler. Counter ise özel bir tanım istenmediği sirece harfleri sayar.
print(Counter(sarki.lower().split()).most_common())#most common en çok tekrar edenden itibaren yazdırır.
