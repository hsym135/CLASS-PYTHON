#public class

class guru1:
    def __init__(self,nama, job):
        self.nama = nama
        self.job = job

pertama = guru1("Pak Firman", "kepala Program RPL")

print(f'{pertama.nama} adalah {pertama.job}')


# protected class

class guru2:
    def __init__(self,nama):
        self._nama = nama 

class kerjaan(guru2):
    def __init__(self, nama, job):
        super().__init__(nama)
        self._job = job

    def output(self):
        print (f'{self._nama} adalah {self._job}')

outputnya = kerjaan('pak Arya','guru RPL')
outputnya.output()


# private class

class guru3:
    def __init__(self,nama):
        self.__nama = nama

    def tampilkan_nama(self):
        print(f'{self.__nama} adalah petugas perpus')

guru = guru3('Pak Ryan')
guru.tampilkan_nama()