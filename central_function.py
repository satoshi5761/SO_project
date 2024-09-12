import os as so
import rich
print = rich.print

class LinuxOS:
    def __init__ (self):

        # menangkap semua directory di 
        # path saat ini
        self.ls_dir = "ls -d */"

        # menampilkan path saat ini
        self.pwd = "pwd"



    def show_current_path(self):
        """
        menampilkan path directory saat ini
        """
        run_command = so.popen(self.pwd)
        read_command = run_command.read().rstrip()
        print(read_command)


    def get_available_directories(self):
        """
        return semua directory pada working directory jika ada
        return None jika tidak ada
        """
        run_command = so.popen(self.ls_dir)
        read_command = run_command.read().rstrip()
        lst_directories = read_command.split('\n')

        if ''.join(lst_directories) == "":
            return None
        else:
            return lst_directories

    
    def change_directory(self, target_directory):
        """
        pindah dari directory saat ini
        ke directory target
        """
        try:
            so.chdir(target_directory)
        except:
            print("/directory tujuan tidak ada")

    