from central_function import LinuxOS, PenghapusSementara
from ASCII_tree_documentation import tembelek
import os
# import rich
# print = rich.print


# util
nama_utilities = ()
if os.name == 'posix':
    nama_utilities = (
        "Show current path",
        "Display directories",
        "Show ASCII Tree",
        "Change directory",
        "QUIT"
    )
elif os.name == 'nt':
    nama_utilities = (
        "Hapus File Sementara",
    )

###########################################################################
###########################################################################
###########################################################################

def display_utilities():
    """
    menampilkan utilities yang tersedia
    """
    for (nomor_opsi, nama_util) in enumerate(nama_utilities):
        print(f"Option [{nomor_opsi + 1}]: {nama_util}")


def utility_A(UBUNTU):
    print(UBUNTU.get_current_path())

def utility_B(UBUNTU):
    print(UBUNTU.get_available_directories())

def utility_C(UBUNTU):
    try:
        depth = int(input("depth (0 untuk maxdepth possible): "))
    except:
        depth = 0

    tembelek(UBUNTU, depth)

def utility_D(UBUNTU):
    UBUNTU.change_directory(input("directory tujuan: "))

def utility_Q():
    """
    untuk QUIT
    """
    return False

###########################################################################
###########################################################################
###########################################################################


def main():

    UBUNTU = LinuxOS()
    penghapus = PenghapusSementara()

    Mahastama = True
    while Mahastama:
        display_utilities()        

        try:
            pilihan_utility = int(input("Pick an option: "))
        except:
            pilihan_utility = 0
            
        if os.name == 'posix':
            if pilihan_utility == 1:
                utility_A(UBUNTU)
            elif pilihan_utility == 2:
                utility_B(UBUNTU)
            elif pilihan_utility == 3:
                utility_C(UBUNTU)
            elif pilihan_utility == 4:
                utility_D(UBUNTU)
            else:
                Mahastama = utility_Q()

        elif os.name == 'nt':
            if pilihan_utility == 1:
                penghapus.hapus_file_sementara()
            else:
                Mahastama = utility_Q()

        print("-" * 50)

main()
