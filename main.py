from central_function import LinuxOS

# tambahkan utility masing-masing
nama_utilities = (
    "show current path",
    "display directories",


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
        else:
            Mahastama = False


        print("-" * 50)

main()