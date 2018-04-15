class token(object):
    kind = ''
    value = ''
    
    def toString(self):
        return self.kind + '  \"' + self.value + '\"'

class lexer(object):
    text = ""
    i = 0

    def init(self, text):
        self.i = 0
        self.text = text
        return self

    def isEOF(self):
        return len(self.text) <= self.i

    def c(self):
        
        if(self.isEOF()):
            print('No more charactor')
        return self.text[self.i]
        
        
    def next(self):
        c = self.c()
        self.i = self.i + 1
        return c

    def skipWhiteSpace(self):
        while(not self.isEOF() and self.c().isspace() ):
            self.next()

    # 演算子かどうか？
    def isSignStart(self, c):
        return c == "=" or c == "+" or c == "-" or c == "*" or c == "/" 
    
    # 数字かどうか
    def isDigitStart(self, c):
        return c.isdigit()

    # アルファベットかどうか
    def isVariableStart(self, c):
        return c.islower()

    def sign(self):
        t = token()
        t.kind = "sign"
        t.value = self.next()
        return t

    def digit(self):
        b = self.next()
        while(not self.isEOF() and self.c().isdigit()):
            b = b + self.next()
        t = token()
        t.kind = "digit"
        t.value = str(b)
        return t

    def variable(self):
        b = self.next()
        while(not self.isEOF() and (self.c().isdigit() or self.c().isalnum())):
            b = b + self.next()
        t = token()
        t.kind = "variable"
        t.value = str(b)
        return t

    def nextToken(self):
        
        self.skipWhiteSpace()
        if self.isEOF():
            return None
        elif self.isSignStart(self.c()):
            return self.sign()
        elif self.isDigitStart(self.c()):
            return self.digit()
        elif self.isVariableStart(self.c()):
            return self.variable()
        else:
            print('not match token ')

    def tokenize(self):
        tokens = []
        t = self.nextToken()
        while (t is not None):
            tokens.append(t)
            t = self.nextToken() 
        return tokens

# debug ```python lexer.py ```
text = " ans1 = 10 + 902  ansA2 = 1 * 2 / 1"
tokens = []
tokens = lexer().init(text).tokenize()
for token in tokens:
    print(token.toString())

