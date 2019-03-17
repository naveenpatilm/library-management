import os

class FileUtil:

    #TODO: fix bug when file has just one line
    @staticmethod
    def read_last_line(filePath):
        with open(filePath, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b"\n":
                return file.readline()
            except OSError:
                print("file is empty")
                return None