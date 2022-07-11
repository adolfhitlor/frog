from os import system
import platform
path='Cellar' if platform.system()=='Darwin' else 'bin'
frog_bash='' if platform.system()=='Darwin' else '-linux'

system(f'cp ./* /usr/local/{path}/frog@0.1/*')
system(f'rm -rf /usr/local/{path}/frog@0.1/install*')
system(f'mv /usr/local/Cellar/frog@0.1/frog{frog_bash} /usr/local/bin/')
system(f'mv /usr/local/bin/frog{frog_bash} /usr/local/bin/frog')
