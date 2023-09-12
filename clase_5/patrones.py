import re

patron = re.compile(r'\bfoo\b')

texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""


# print(patron.match(texto))
# m = patron.match('foo bar')
# print(m)
#<re.Match object; span=(0, 3), match='foo'>#
# En el span=(0,3) se marca el inciio(0) y fin del patron(3) sin inclir estas posiciones

s= patron.search(texto)
# print(s)
#<re.Match object; span=(4, 7), match='foo'>#
# En el span=(4,7) se marca el inciio(4) y fin del patron(7) sin inclir estas posiciones
print(s.group(),s.start(),s.end(),s.span()) 
#foo 4 7 (4, 7)#

# fa = patron.findall(texto)
# print(fa)
# #['foo', 'foo', 'foo', 'foo']#
# # Devuelve una lista con todas las coincidencias, solo los "foo" no los "barfoo" ni "foofoo"

# fi = patron.finditer(texto)
# print(fi)
# #<callable_iterator object at 0x7f9b1c0b6a90>#
# print(next(fi))
# #<re.Match object; span=(5, 8), match='foo'>#
# print(next(fi))
# #<re.Match object; span=(13, 16), match='foo'>#
# print(next(fi))
# #<re.Match object; span=(34, 37), match='foo'>#