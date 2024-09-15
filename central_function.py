import os as so

class LinuxOS:
    def __init__ (self):

        # menangkap semua directory di 
        # path saat ini ( hanya directory )
        self.ls_dir = "ls -d */"

        # menampilkan path saat ini
        self.pwd = "pwd"

        # menangkap file-file di
        # path saat ini
        self.ls_file = "ls -p | grep -v /"

    def get_current_path(self):
        """
        return path directory saat ini
        """
        run_command = so.popen(self.pwd)
        read_command = run_command.read().rstrip()
        return read_command


    def change_directory(self, target_directory):
        """
        pindah dari directory saat ini
        ke directory target
        """
        try:
            so.chdir(target_directory)
        except:
            print("/directory tujuan tidak ada")


    def get_available_directories(self):
        """
        return semua directory pada working directory jika ada
        return empty [] jika tidak ada
        """
        run_command = so.popen(self.ls_dir)
        read_command = run_command.read().rstrip()
        lst_directories = read_command.split('\n')

        if ''.join(lst_directories) == "":
            return []
        else:
            return lst_directories

    
    def get_available_files(self):
        """
        return semua file-file pada working diretory jika ada
        return empty [] jika tidak ada
        """
        run_command = so.popen(self.ls_file)
        read_command = run_command.read().rstrip()
        lst_files = read_command.split('\n')

        if "".join(lst_files) == "":
            return []
        else:
            return lst_files

    