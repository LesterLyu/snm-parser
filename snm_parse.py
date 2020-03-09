from lark import Lark

grammar = open("grammar.lark", "r").read()

s0 = 'age1 > 10 || age2 < 20 && age3 < 30 || aaa == "bbb"'
s1 = "(age > 10 and age < 20)"
s2 = '(nationality in ["Israel"]'
# print( l.parse("Hello, World!") )


if __name__ == "__main__":
    # TO_DO
    parser = Lark(grammar, parser='lalr')
    print(parser.parse('[1] in [1, 2, [1+1], "str2", true]'))
