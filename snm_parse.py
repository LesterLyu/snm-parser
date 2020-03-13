from lark import Lark, Transformer, Tree
import sys

grammar = open("grammar.lark", "r").read()


class SNMTransformer(Transformer):


    # Token transformations
    NUMBER = float
    STRING = str

    def BOOLEAN(self, boolean):
        return True if boolean == 'true' else False

    def FIELD(self, field):
        # TODO: lookup data base
        if field == 'age':
            return 20
        return 100

    def terminal(self, data):
        return data[0]

    # Array and array operation (in)
    def array(self, items):
        return list(items)

    def in_exp(self, exps):
        if not isinstance(exps[2], list):
            raise 'Invalid use of in operator.'

        if isinstance(exps[0], list):
            return set(exps[0]).issubset(set(exps[2]))
        return exps[0] in exps[2]    

    # Arithmetic operations
    def add_sub_exp(self, exps):
        if exps[1] == '+':
            return exps[0] + exps[2]
        return exps[0] - exps[2]

    def mul_div_mod_exp(self, exps):
        if exps[1] == '*':
            return exps[0] * exps[2]
        elif exps[1] == '/':
            return exps[0] / exps[2]
        else:
            return exps[0] % exps[2]

    def unary_exp(self, exps):
        if exps[0] == '+':
            return exps[1]
        else:
            return -exps[1]

    # Logical operations
    def or_exp(self, exps):
        return exps[0] or exps[2]

    def and_exp(self, exps):
        return exps[0] and exps[2]

    def eq_neq_exp(self, exps):
        if exps[1] == '==':
            return exps[0] == exps[2]
        else:
            return exps[0] != exps[2]
            
    def not_exp(self, exps):
        return not exps[1]
    
    # Compare oprations
    def compare_exp(self, exps):
        if exps[1] == '<':
            return exps[0] < exps[2]
        elif exps[1] == '>':
            return exps[0] > exps[2]
        elif exps[1] == '<=':
            return exps[0] <= exps[2]
        elif exps[1] == '>=':
            return exps[0] >= exps[2]



s0 = 'age1 > 10 || age2 < 20 && age3 < 30 || aaa == "bbb"'
s1 = "(age > 10 && age < 20)"
s2 = 'nationality in ["Israel"]'

if __name__ == "__main__":
    text = s0

    if len(sys.argv) != 1:
        text = sys.argv[1]
    
    if len(text) == 0:
        exit(0)

    parser = Lark(grammar, parser='lalr')
    transformer = SNMTransformer()

    tree = parser.parse(text)
    print(transformer.transform(tree))

