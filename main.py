













class Stack:
    
    max_size = 4
    
    def __init__(self) -> None:
        self.top = 0
        self.v = [0] * self.max_size

    def push(self, c) -> None:
        if (self.top == self.max_size): raise(OverflowError)
        self.v[self.top] = c
        self.top += 1

    def pop(self):
        if (self.top == 0 ): raise(IndexError)
        self.top -= 1
        return self.v[self.top]



TOKEN = {
    "ALPHA":        0,
    "NUMBER":       1,
    "END":          2,
    "PLUS":         "+",
    "MINUS":        "-",
    "MULTIPLY":     "*",
    "DIVIDE":       "/",
    "ASSIGN":       "=",
    "LPARENTHESIS": "(",
    "RPARENTHESIS": ")",
    "PRINT":        ";"
}

cur_tok = TOKEN["PRINT"]

def expr(get):
    """
    bool get
    term(bool) - член алгебраического выражения
    Обрабатывает сложение и вычитание   
    """
    left = term(get)

    while(True):
        if cur_tok == TOKEN["PLUS"]:
            left += term(True)
        elif cur_tok == TOKEN["MINUS"]:
            left -= term(True)
        else: return left
    return

def term(get):
    pass
def prim(get):
    pass

if __name__ == "__main__":
    my_stack = Stack()
