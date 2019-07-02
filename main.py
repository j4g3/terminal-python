import os
import glob
files = open('dados.dll')
data = files.read()
files.close

#desktop of user

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','--']


user_info = os.path.expanduser('~')

location_default = os.path.expanduser('~\\Desktop')
location = os.path.expanduser('~\\Desktop')
desktop = os.path.expanduser(f'{location}').replace(f'{user_info}', f'{data}')

os.chdir(location)

help_git = '''

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.

'''



while True:
        command = input(f'{desktop}:# ')
        
        if command == 'ls':
            #listing files
            os.chdir(location)
            print(location)
            location = os.getcwd()
            desktop = os.path.expanduser(f'{location}').replace(f'{user_info}', f'{data}')
            
            for file in glob.glob("*"):
                print(file)
        
        elif(command[0] == 'c' and command[1] == 'd'):
            #browsing the files
            location = str(command).replace("cd", "").replace(" ","")
            
            if(command.count("..")):
            
                os.chdir('../')
                location = os.getcwd()
                desktop = os.path.expanduser(f'{location}').replace(f'{user_info}', f'{data}')
            
            else:

                command = command.replace("cd ", "")
                os.chdir(command)
                location = os.getcwd()
                desktop = os.path.expanduser(f'{location}').replace(f'{user_info}', f'{data}')
        
        elif command == 'clear':
            #clean in terminal
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif command == 'refresh':
            #restart of terminal

            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python refresh.py')
            
            exit()
        elif(command.count('cat ')):
            command = command.replace("cat ", "")
            cat = open(f'{command}', 'r')
            content = cat.readlines()
            #listing content of file
            print('\n')
            
            for line in content:
                print(line)
            cat.close()
            
            print('\n')
        elif command[0] == 'g' and command[1] == 'i' and command[2] == 't':
            os.system(command)
        elif command == '':
            pass