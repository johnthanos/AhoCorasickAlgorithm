# AhoCorasickAlgorithm
My implementation of the Aho Corasick Algorithm for pattern matching. 

With 2 functions to create the Automaton (a trie created with the goto function and with extra edges implemented by the 
failure function)

Go to function of the Aho Corasick Algorithm, it  simply follows edges of Trie (automaton)  of all patterns in pat. It is 
represented as a dictionary g{} where we store next state, for current state with the character we read, a list d of the 
depth of each state, so we can count skipped compares, and an output list for the each nodes.

Fail Function of the Aho Corasick Algorithm, This function stores all edges that are followed when current character doesn't 
have edge in Trie (Automaton).

Example run with pattern pat, and string s

    pat = ['GAATG', 'CTA', 'CCGT', 'AC', 'ATG', 'TGT']
    s = 'CTAATGTTGAATGGCCACTACCGTGAATGCCGTGTGAATGCTA'
Expected output:

The goto function is:
{(0, 'T'): 16, (0, 'G'): 1, (3, 'T'): 4, (4, 'G'): 5, (6, 'C'): 9, (16, 'G'): 17, (9, 'G'): 10, (6, 'T'): 7, (1, 'A'): 2, (14, 'G'): 15, (0, 'A'): 12, (0, 'C'): 6, (17, 'T'): 18, (12, 'C'): 13, (7, 'A'): 8, (10, 'T'): 11, (12, 'T'): 14, (2, 'A'): 3}

The failure function is:
[0, 0, 12, 12, 14, 15, 0, 16, 12, 6, 1, 16, 0, 6, 16, 17, 0, 1, 16, 0]

Number of compares 42

We skip 7 compares

Patterns found :,CTA,ATG,TGT,GAATG,ATG,AC,CTA,AC,CCGT,GAATG,ATG,CCGT,TGT,GAATG,ATG,CTA,

GAATG pattern is found 3 times 

CTA pattern is found 3 times 

CCGT pattern is found 2 times 

AC pattern is found 2 times 

ATG pattern is found 4 times 

TGT pattern is found 2 times 


This implementation was made by me (Ioannis Thanos) for the course Bioinformatics (Βιοπληοφορική) at Computer Engineer and Informatics Department of the Polytechnic Branch of the University of Patras. 
