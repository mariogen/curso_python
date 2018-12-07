
"""
Essa é a documentação do módulo

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""


print(__doc__)

dash = '-'*5

print(
    dash +
    ' a seguir, o mesmo texto, porém sem o "alinhamento manual" ' +
    dash + '\n'
)

for p in __doc__.strip().split('\n\n'):
    print(' '.join(p.split()), end='\n\n')
