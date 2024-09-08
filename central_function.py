import os

class LinuxOS:
    def __init__ (self):
        # list of necessary Linux commands
        self.ls_dir = "ls -d */"
        self.cd = "cd"

    def get_current_directories(self):
        run_command = os.popen(self.ls_dir)
        read_command = run_command.read().rstrip()
        lst_directories = read_command.split('\n')

        print(lst_directories)

class WindowsOS:
    def __init__ (self):
        pass

debian = LinuxOS()
debian.get_current_directories()
