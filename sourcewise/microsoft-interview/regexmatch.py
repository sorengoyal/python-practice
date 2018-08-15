class Rule:
    def __init__(self, rule, minreps, maxreps):
        self.rule = rule
        self.minreps = minreps
        self.maxreps = maxreps

    def apply(self, ch):
        if self.maxreps == 0:
            return False
        else:
            self.maxreps = self.maxreps-1 if self.maxreps > 0 else -1
            return self.rule(ch)

def isSymbol(ch):
    return ch.isalnum() or ch == '.'

def isGroup(ch):
    return False

def parseRegex(exp):
    ruleStack = []
    for i,ch in enumerate(exp):
        if isSymbol(ch):
            apply, minreps, maxreps = None, None, None
            if ch == '.':
                apply = lambda c: True
            else:
                apply = lambda c: c==ch
            try:
                if exp[i+1] == '+':
                    minreps = 1
                    maxreps = -1
                elif exp[i+1] == '*':
                    minreps = 0
                    maxreps = -1
                else:
                    minreps = 2
                    maxreps = 1
            except IndexError as e:
                minreps = 1
                maxreps = 1
            ruleStack.append(Rule(apply, minreps, maxreps))
        elif isGroup(ch):
            pass
        else:
            continue

    return ruleStack


def match(regex, exp):
    n = len(exp)
    rules = parseRegex(regex)
    m = len(rules)
    M = [[None]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        M[i][m] = True
    for j in range(m+1):
        M[n][j] = False
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if rules[j].apply(exp[i]):
                M[i][j] = M[i+1][j+1] or M[i+1][j]
            else:
                M[i][j] = M[i][j+1]

    for i in range(n+1):
        for j in range(m+1):
            print M[i][j],
        print ''


    return M[0][0]


print(match('a+b.b*','kaaab9bb'))