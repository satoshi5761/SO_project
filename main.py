from central_function import LinuxOS
from ASCII_tree import solve
# import rich
# print = rich.print


# tambah util
nama_utilities = (
    "Show current path",
    "Display directories",
    "Change directory",

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
        print(f"Option {nomor_opsi + 1}: {nama_util}")

###########################################################################
###########################################################################
###########################################################################


def main():

    UBUNTU = LinuxOS()
    solve(UBUNTU, 0)

    Mahastama = True
    while Mahastama:
        display_utilities()        

        try:
            pilihan_utility = int(input("Pick an option: "))
        except:
            pilihan_utility = 0
        

        if pilihan_utility == 1:
            UBUNTU.show_current_path()
        elif pilihan_utility == 2:
            print(UBUNTU.get_available_directories())
        elif pilihan_utility == 3:
            UBUNTU.change_directory(input("directory tujuan: "))
        else:
            Mahastama = False


        print("-" * 50)

main()