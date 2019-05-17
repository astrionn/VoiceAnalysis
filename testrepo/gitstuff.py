import time
import subprocess
import os
gitcommands=['add','commit','push','clone','fetch']
dir_path = os.path.dirname(os.path.realpath(__file__))

def doGit(gitaction,repoDir=dir_path,fileName=None,commitMessage=None):
    cmd = 'git '
    if gitaction in [gitcommands[0],gitcommands[3]]: #add,clone

        cmd += gitaction +" "+ fileName
    elif gitaction == gitcommands[1]: #commit
        cmd += gitaction +  ' -am "%s"'%commitMessage
    elif gitaction in [gitcommands[2],gitcommands[4]]: #push,fetch
        cmd += gitaction

    
    
    print(cmd)
    pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
    (out, error) = pipe.communicate()
    pipe.wait()
    return


