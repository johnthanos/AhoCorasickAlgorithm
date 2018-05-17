def gotofunc(pat):
    """
    Go to function of the Aho Corasick Algorithm, it  simply follows edges
    of Trie (automaton)  of all patterns in pat. It is represented as a
    dictionary g{} where we store next state for current state for the character
    we read, a list d of the depth of each state and an output list for the each nodes.
    :param pat: list of patterns to create the Trie
    :return: g the dictionary of states, output of each state, d list of depths of each state of the automaton
    """

    newstate = 0
    g = {}
    d = [0 for i in range(20)]
    output = ["" for i in range(20)]
    d[0] = 0
    for i in range(0, len(pat)):
        state = 0
        j = 0

        p = list(pat[i])
        while (state, p[j]) in g:
            state = g[(state, p[j])]
            j += 1
        for k in range(j, len(p)):
            newstate += 1
            g[state, p[k]] = newstate
            d[newstate] = d[state] + 1
            state = newstate
        output[state] = '{},'.format(pat[i])
    # Initialasing the 1st states
    for a in {'C', 'T', 'A', 'G'}:
        while not g[(0, a)]:
            g[(0, a)] = 0

    return g, output, d


def failfunc(g, output):
    """
    Fail Function of the Aho Corasick Algorithm, This function stores all edges that are
          followed when current character doesn't have edge in Trie (Automaton).
    :param g: a dictionary with ste states (nodes) of the Automaton (Trie)
                and the letter we read with the next state to go
    :param output: a list with the output for each state (node)
    :return: fail: a list with the next state for current state,
    and updated output for subpatterns included in other patterns
    """
    # Initialising fail list, if nothing is found just return to first state
    fail = [0 for t in range(20)]

    queue = []
    for a in {'C', 'T', 'A', 'G'}:
        if g[(0, a)] != 0:
            queue.append(g[(0, a)])
            fail[g[(0, a)]] = 0
    while queue:
        r = queue.pop(0)
        for a in {'C', 'T', 'A', 'G'}:
            if (r, a) in g:
                s = g[(r, a)]

                queue.append(s)
                state = fail[r]
                while not ((state, a) in g):
                    state = fail[state]

                fail[s] = g[(state, a)]
                output[s] = '{}{}'.format(output[s], output[fail[s]])
    return fail, output


if __name__ == "__main__":
    """
    Example run with pattern pat, and string s
    """

    pat = ['GAATG', 'CTA', 'CCGT', 'AC', 'ATG', 'TGT']
    s = 'CTAATGTTGAATGGCCACTACCGTGAATGCCGTGTGAATGCTA'

    # Creating the Automaton

    g, output, d = gotofunc(pat)  # calling goto function
    fail, output = failfunc(g, output)  # calling failure function

    # Several counters
    state = 0
    skip_count = 0
    patterns_found = ","
    print('The goto function is:\n')
    print(g)
    print('The failure function is:\n')
    print(fail)

    # Pattern Matching Machine Algorithm
    for i in range(0, len(s)):
        while not ((state, s[i]) in g):

            state = fail[state]
            if not state: skip_count += 1  # counting skips
        state = g[(state, s[i])]
        if output[state]:
            patterns_found = '{}{}'.format(patterns_found, output[state])

    # print output[state]
    # print i
    print('\nNumber of compares {}\n'.format(i))
    print('\nWe skip {} compares\n'.format(skip_count))
    print('Patterns found :{}'.format(patterns_found))

    # counting instances of each pattern
    for j in range(0, 6):
        c = 0
        pat_count = 0
        while patterns_found.find(',{},'.format(pat[j]), c) > -1:
            pat_count += 1
            c = patterns_found.find(',{},'.format(pat[j]), c) + len(pat[j])
        print('{} pattern is found {} times \n'.format(pat[j], pat_count))
