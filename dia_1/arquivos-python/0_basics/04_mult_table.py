

"Imprime Tabuada"

n = 10

for i in range(1,n+1):
    for j in range(1,n+1):

        end=('\n' if j%n==0 else '')

        print(' '+'{0:3d}'.format(i*j), end=end)

