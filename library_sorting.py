import sys
import argparse
import json
import sparse as sparse

def main():
    if len(sys.argv) < 2 :
        print("Usage:  python library_sorting.py file.json")
        return
    fname = sys.argv[1]
    file = open(fname, 'r')
    data = json.load(file)
    nn = data['nn']
    mm = data['mm']
    k = data['k']
    x = data['x']
    actions = data['actions']
    sp = sparse.sparse(nn, mm, k, x)
    sp.print_data()

    for  action in actions:      
         if action['action'] == 'insert':
             key = action['key']
             sp.insert(key)
         elif action['action'] == 'delete':
             key = action['key']
             sp.delete(key)
         elif action['action'] == 'lookup':
             key = action['key']
             sp.binarySearch(key)
         sp.print_data()
   
    
    


main()