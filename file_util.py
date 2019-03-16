import os

class FileUtil:
    @staticmethod
    def readLastLine(filePath):
        with open(filePath, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b"\n":
                    file.seek(-2, os.SEEK_CUR)
                return file.readline()
            except OSError:
                print("file is empty")
                return None