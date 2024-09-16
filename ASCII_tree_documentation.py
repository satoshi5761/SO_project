import rich
print = rich.print

"""
menampilkan directory saat ini
dalam bentuk ASCII art tree
dengan depth berdasarkan input user
input = 0 untuk maxdepth

example output:
pwd/
|
├── dir1/ # depth 1
|   └── dirdir1/ # depth 2
|       ├── dirdirdir1 # depth 3
|       |   ├── dirdirdirdir1 # depth 4
|       |   |   └── x.txt # depth 5
|       |   └── q.txt # depth 4
|       └── q.txt # depth 3
|
├── dir2/ # 1
|   └── dirdir2/ # 2
|
├── test1.txt # 1
├── test2.txt # 1
└── main.py # 1


solusi?
1. simpan terlebih dahulu directory dan file dalam node
sesuai dengan input depth
2. traverse node-node yang sudah jadi dari yang paling atas
sampai paling akhir satu persatu, setiap pergantian node
akan menghasilkan output yang sesuai

rules output:
1. jika node berupa children yang paling akhir maka
gunakan symbol └──, jika tidak maka gunakan symbol ├──
2. kedalaman depth diperlukan untuk menghasilkan output symbol | sebanyak (depth - 1) kali

"""

class Node:
    def __init__(self, name):
        self.parent = None
        self.name = name
        self.short_name = ""
        self.child_directories = []
        self.child_files = []
        self.edges = 0

    def build_tree(self, UBUNTU, depth, stacking):
        """
        --- input file system ---
        UBUNTU sebagai manuever
        depth sebagai indikator kapal selam
        stacking sebagai acuan kembali
        """
        if depth <= 0:
            return # berhenti sampai sini
        else:

            available_directories = UBUNTU.get_available_directories()
            for directory in available_directories:
                current_Node = Node(self.name + directory)
                self.child_directories.append(current_Node)

                current_Node.short_name = directory

                current_Node.edges = len(stacking)

                stacking.append(self.name + directory)
                UBUNTU.change_directory(stacking[-1])

                current_Node.child_files = UBUNTU.get_available_files()

                current_Node.build_tree(UBUNTU, depth - 1, stacking)
                UBUNTU.change_directory(stacking.pop())

    def traverse(self):
        for directory in self.child_directories:
            print(directory.name, directory.edges)
            print(directory.child_files)
            directory.traverse()

    def pipe_edges(self, depth):
        """
        GAGAL, saya tidak sadar ada edge case
        """
        panjang_space = 3
        for _ in range(depth - 1):
            print('|' + ' ' * panjang_space, end='')

    def new_pipe(self, lst):
        """
        pembaruan, fixed edge cases
        """
        for x in lst:
            if x is True:
                print('|' + ' ' * 3, end='')
            else:
                print(' ' * 4, end='')

    def pretty_printing_directories(self, lst):
        for (i, directory) in enumerate(self.child_directories):
            directory.new_pipe(lst)
            
            if i == len(self.child_directories) - 1:
                if not self.child_files:
                    print('└──', directory.short_name)
                    lst.append(False)
                else:
                    print('├──', directory.short_name)
                    lst.append(True)
            else:
                print('├──', directory.short_name)
                lst.append(True)
            
            directory.pretty_printing_directories(lst)

            directory.pretty_printing_files(lst)

            lst.pop()

    def pretty_printing_files(self, lst):
        if self.child_files:
            for (j, file) in enumerate(self.child_files):
                self.new_pipe(lst)
                if j == len(self.child_files) - 1:
                    print('└──', file)
                else:
                    print('├──', file)

            self.new_pipe(lst)
            print()
        else:
            if not self.child_directories:
                self.new_pipe(lst)
                print()

def tembelek(UBUNTU, depth):
    if depth == 0: depth = float('inf')

    root = Node(UBUNTU.get_current_path() + '/')
    root.child_files = UBUNTU.get_available_files()

    stacking = [root.name]
    root.build_tree(UBUNTU, depth, stacking)

    print(root.name)
    print('|')
    root.pretty_printing_directories([])
    root.pretty_printing_files([])

    UBUNTU.change_directory(root.name)

