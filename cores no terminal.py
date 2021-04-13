'''
style 
0 - none        
1 - bold        
4 - underline   
7 - negative

text
30 - white
31 - red
32 - green
33 - yellor
34 - blue

back
40 - white
41 - red
42 - green
43 - yellow
44 - blue    
 
 Modo de usar: \033[style;text;backm....\033[m
 '''
#-------------------------------------------------------
from os import system
system('cls')
print('\033[;31;40m-=\033[m'*30)
name = '\033[4;33;40mCORES NO TERMNIAL\033[m'
print('{:^70}'.format(name))
print('\033[0;31;40m-=\033[m'*30)