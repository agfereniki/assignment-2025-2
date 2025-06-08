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
    print(sp.isDummy(0),sp.isDummy(1))
    sp.insert(5)
    sp.print_data()
    sp.insert(6)
    sp.print_data()
    sp.insert(3)
    #sp.print_data()
    sp.insert(4)
    sp.print_data()
    sp.insert(10)
    sp.print_data()
    sp.insert(8)
    sp.print_data()
    sp.insert(7)
    sp.print_data()
    # for  action in actions:      
    #     if action['action'] == 'insert':
    #         key = action['key']
    #         sp.insert(key)
    #     elif action['action'] == 'delete':
    #         key = action['key']
    #         sp.delete(key)
    #     elif action['action'] == 'lookup':
    #         key = action['key']
    #         index = sp.binarySearch(key)
    #         if index != -1:
    #             print(f"Key {key} found at index {index}")
    #         else:
    #             print(f"Key {key} not found")
    #     sp.print_data()
   
    
    


main()