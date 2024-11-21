import os
import shutil
import tempfile
from pathlib import Path
import datetime


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
        run_command = os.popen(self.pwd)
        read_command = run_command.read().rstrip()
        return read_command


    def change_directory(self, target_directory):
        """
        pindah dari directory saat ini
        ke directory target
        """
        try:
            os.chdir(target_directory)
        except:
            print("/directory tujuan tidak ada")


    def get_available_directories(self):
        """
        return semua directory pada working directory jika ada
        return empty [] jika tidak ada
        """
        run_command = os.popen(self.ls_dir)
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
        run_command = os.popen(self.ls_file)
        read_command = run_command.read().rstrip()
        lst_files = read_command.split('\n')

        if "".join(lst_files) == "":
            return []
        else:
            return lst_files


class PenghapusSementara:
    def __init__(self):
        self.direktori_sementara = tempfile.gettempdir()
        self.jumlah_file_dihapus = 0
        self.jumlah_folder_dihapus = 0

    def hapus_file_di_sementara(self):
        daftar_file = os.listdir(self.direktori_sementara)

        if not daftar_file:
            print("Tidak ada file sementara yang perlu dihapus.")
            return

        for nama_file in daftar_file:
            jalur_file = os.path.join(self.direktori_sementara, nama_file)
            try:
                if os.path.isfile(jalur_file) or os.path.islink(jalur_file):
                    os.unlink(jalur_file)
                    self.jumlah_file_dihapus += 1
                elif os.path.isdir(jalur_file):
                    shutil.rmtree(jalur_file)
                    self.jumlah_folder_dihapus += 1
            except Exception as e:
                print(f"Gagal menghapus {jalur_file}. Alasan: {e}")

        print(f"\nJumlah file yang dihapus: {self.jumlah_file_dihapus}")
        print(f"Jumlah folder yang dihapus: {self.jumlah_folder_dihapus}")

    def hapus_file_sementara(self):
        print(f"Lokasi folder sementara: {self.direktori_sementara}")
        
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus semua file di {self.direktori_sementara}? (y/n): ").lower()
        if konfirmasi == 'y':
            self.hapus_file_di_sementara()
            print("Penghapusan file sementara selesai.")
        else:
            print("Penghapusan dibatalkan.")

class Search_and_Sort_Files:
    # function untuk search file
    def search_files(self, directory, keyword="", extension=None):
        # ini untuk nyari file di suatu direktori berdasarkan keyword dan ekstensi yang di-input sama user..
        try :
            files = []
            for root, dirs, filenames in os.walk(directory):
                for namafile in filenames:
                    if keyword.lower() in namafile.lower() and (not extension or namafile.endswith(extension)):
                        files.append(Path(root)/namafile)
            return files
        except Exception as jenisError:
            print(f"Error: {jenisError}")
            return []

    # function untuk sort file
    def sort_files(self, files, sortby='nama', reverse=False):
        # ini untuk ngurutin file berdasarkan nama, ukuran, atau waktu edit/modifikasi (usernya bisa milih)..
        if sortby == 'nama':
            return sorted(files, key=lambda x: x.name, reverse=reverse)
        elif sortby == 'ukuran':
            return sorted(files, key=lambda x: x.stat().st_size, reverse=reverse)
        elif sortby == 'waktu edit':
            return sorted(files, key=lambda x: x.stat().st_mtime, reverse=reverse)
        else:
            print("Error.. Input yang Anda masukkan salah, masukkan 'nama','ukuran', atau 'waktu edit'")
            return files
        
    def run(self):
        directory = input("\nMasukkan lokasi directory yang ingin diakses : ").strip()
        if not os.path.exists(directory):
            print("Error: Directory yang Anda masukkan tidak ada")
            exit()
        
        kataKunci = input("\nMasukkan nama file yang ingin dicari (kosongkan jika Anda ingin mencari semua file di folder tersebut) :\n>> ").strip()
        jenisFile = input("Masukkan jenis file (misalnya .txt, .pdf, .py, atau kosongkan jika Anda ingin mencari semua file):\n>> ").strip()
        jenisFile = None if not jenisFile else jenisFile

        file_ditemukan = self.search_files(directory, kataKunci, jenisFile)
        if not file_ditemukan:
            print("File yang Anda cari tidak ditemukan.")
            exit()
        
        print(f"\nDitemukan {len(file_ditemukan)} file yang sesuai dengan kriteria yang Anda cari :")
        for file in file_ditemukan:
            print(f"- {file}")
        
        urutan = input("\nUrutkan file berdasarkan ('nama', 'ukuran', 'waktu edit'): ").strip().lower()
        reverse_sort = input("Urutkan dari yang terbesar ke terkecil? (y/n): ").strip().lower() == 'y'

        sorted_files = self.sort_files(file_ditemukan, sortby=urutan, reverse=reverse_sort)

        print("\nFile berhasil diurutkan!")
        print("\nFile Anda:")
        for file in sorted_files:
            print(f"- {file} (Size: {file.stat().st_size} bytes, Diedit pada: {file.stat().st_mtime})")





class BackUp_Files:
    def backup_data(self, source_dir, backup_dir):
        if not os.path.exists(source_dir):
            print(f"Direktori'{source_dir}' tidak ditemukan!")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

        try:
            shutil.copytree(source_dir, backup_path)
            print(f"Backup '{source_dir}' dibuat di '{backup_path}'")
        except Exception as e:
            print(f"Terjadi error: {e}!")

    def select_directory(self, title):
        directory = input(title)
        return directory

    def run(self):
        source_directory = self.select_directory("Pilih direktori asal yang akan di backup: ")
        if not source_directory:
            print("Tidak ada direktori asal yang dipilih. Selesai.")
            exit()

        backup_directory = self.select_directory("Pilih direktori untuk backup: ")
        if not backup_directory:
            print("Tidak ada direktori backup yang dipilih. Selesai.")
            exit()

        self.backup_data(source_directory, backup_directory)