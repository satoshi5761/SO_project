from central_function import LinuxOS, PenghapusSementara, Search_and_Sort_Files, BackUp_Files
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
        "Change directory",
        "Show ASCII Tree",
        "Search and Sort Files",
        "BackUp Files",
        "Hapus File Sementara",
        "QUIT"
    )
elif os.name == 'nt':
    nama_utilities = (
        "Hapus File Sementara",
        "Search and Sort Files",
        "BackUp Files",
        "QUIT"
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

def utility_E():
    SSF = Search_and_Sort_Files()
    SSF.run()

def utility_F():
    BackUp = BackUp_Files()
    BackUp.run()

def utility_G():
    penghapus = PenghapusSementara()
    penghapus.hapus_file_sementara()

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
                utility_D(UBUNTU)
            elif pilihan_utility == 4:
                utility_C(UBUNTU)
            elif pilihan_utility == 5:
                utility_E()
            elif pilihan_utility == 6:
                utility_F()
            elif pilihan_utility == 7:
                utility_G()
            else:
                Mahastama = utility_Q()

        elif os.name == 'nt':
            if pilihan_utility == 1:
                utility_G()
            elif pilihan_utility == 2:
                utility_E()
            elif pilihan_utility == 3:
                utility_F()
            else:
                Mahastama = utility_Q()

        print("-" * 50)

main()
