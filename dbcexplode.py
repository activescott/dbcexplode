"""explodes the dbc files from databricks into more useful python/sql/markdown files."""
from __future__ import print_function
import json
import sys
import os

def getLangPrefix(cmdstr):
  prefix = cmdstr.splitlines()[0] if len(cmdstr) > 0 else ''

  if len(prefix) > 0 and prefix[0] == '%':
    prefix = prefix[1:]
  else:
   prefix = ''

  return prefix
    
def getExtension(notebook, command):
  extMap = {
    'python': 'py',
    'md': 'md',
    'sql': 'sql',
  }
  cmdstr = command['command']
  if len(cmdstr) == 0:
    return
  
  prefix = getLangPrefix(cmdstr)
  ext = extMap[prefix] if prefix in extMap else None
  
  if ext is None:
    ext = extMap[notebook['language']]
    
  return ext if ext is not None else '' 
  
def outdir(inputFile):
  outdir = inputFile + '-exploded'
  if not (os.path.exists(outdir) and os.path.isdir(outdir)):
    os.mkdir(outdir)
  return outdir

def processfile(filepath):
  print('loading file ', filepath)
  with open(filepath) as f:
    try:
      notebook = json.loads(f.read())
    except ValueError, e:
      notebook = None
      pass

  # ensure it is a notebook
  if notebook == None or (not notebook['version'] == 'NotebookV1'):
    print('SKIPPING file, ', filepath, '. Not a notebook.')
    return

  # prepare output dir:
  dir = outdir(filepath)

  notebookName = notebook['name']
  commands = notebook['commands']
  commandNo = 0
  for command in commands:
    commandNo += 1
    cmdstr = command['command']
    if len(cmdstr) > 0:
      if len(getLangPrefix(cmdstr)) > 0:
        # it has a language prefix (e.g. %python ), so remove that prefix
        lines = cmdstr.splitlines()
        cmdstr = '\n'.join(lines[1:])
      
      ext = getExtension(notebook, command)
      path = os.path.join(dir, notebookName + str(commandNo) + '.' + ext)
      
      with open(path, 'w') as f:
        f.write(cmdstr.encode('utf-8'))

def main():
  if len(sys.argv) != 2:
    print('sys.argv', sys.argv)
    print("""
    Usage: dbc-explode <dbc_file>

    Run with example jar:
    dbc-explode /path/file.dbc
    """, file=sys.stderr)
    exit(-1)
  
  #load file:
  filepath = os.path.abspath(sys.argv[1])
  if os.path.isfile(filepath):
    processfile(filepath)
  elif os.path.isdir(filepath):
    for dir, dirs, files in os.walk(filepath):
      for filepath in files:
        processfile(os.path.join(dir, filepath))


if __name__ == "__main__":
  main()