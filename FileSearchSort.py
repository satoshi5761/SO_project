# File Search and Sort

import os
from pathlib import Path

# function untuk search file
def search_files(directory, keyword="", extension=None):
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
def sort_files(files, sortby='nama', reverse=False):
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


# Main Program
if __name__ == "__main__":
    print("=== Sebuah Program File Search and Sort ===")
    
    directory = input("\nMasukkan lokasi directory yang ingin diakses : ").strip()
    if not os.path.exists(directory):
        print("Error: Directory yang Anda masukkan tidak ada")
        exit()
    
    kataKunci = input("\nMasukkan nama file yang ingin dicari (kosongkan jika Anda ingin mencari semua file di folder tersebut) :\n>> ").strip()
    jenisFile = input("Masukkan jenis file (misalnya .txt, .pdf, .py, atau kosongkan jika Anda ingin mencari semua file):\n>> ").strip()
    jenisFile = None if not jenisFile else jenisFile

    file_ditemukan = search_files(directory, kataKunci, jenisFile)
    if not file_ditemukan:
        print("File yang Anda cari tidak ditemukan.")
        exit()
    
    print(f"\nDitemukan {len(file_ditemukan)} file yang sesuai dengan kriteria yang Anda cari :")
    for file in file_ditemukan:
        print(f"- {file}")
    
    urutan = input("\nUrutkan file berdasarkan ('nama', 'ukuran', 'waktu edit'): ").strip().lower()
    reverse_sort = input("Urutkan dari yang terbesar ke terkecil? (y/n): ").strip().lower() == 'y'

    sorted_files = sort_files(file_ditemukan, sortby=urutan, reverse=reverse_sort)

    print("\nFile berhasil diurutkan!")
    print("\nFile Anda:")
    for file in sorted_files:
        print(f"- {file} (Size: {file.stat().st_size} bytes, Diedit pada: {file.stat().st_mtime})")