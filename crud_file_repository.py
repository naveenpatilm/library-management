from file_util import FileUtil
from exception import ValueNotFound

class CrudFileRepository(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def save(self):
        with open(self.filePath, 'a+') as file:
            if self.id is None:
                lastLine = FileUtil.readLastLine(self.filePath)
                self.id = 1 if lastLine is None else (int(lastLine.decode("utf-8").split(',')[0])) + 1
                bookDetails = []
                for index, attr in enumerate(self.__dict__.values()):
                    if index != len(self.__dict__.values()) - 1:
                        bookDetails.append(attr)
                file.write((','.join(map(str, bookDetails)) + '\n'))
            else:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(str(self.id) + ','):
                        line = ',".join(map(str, self.__dict__.values()).append("\n"))'
                        file.writelines(lines)
                        return
                raise ValueNotFound("record not found for id - " + str(self.id))

    def findAll(self):
        fileContent = []
        with open(self.filePath, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                fileContent.append(line.split(','))
        return fileContent    


    def deleteById(self, id):
        with open(self.filePath, "rw") as file:
            lines = file.readlines()
            for lineNumber, line in enumerate(lines[:]):
                if line.startswith(str(id) + ','):
                    del lines[lineNumber]
                    return
            raise ValueNotFound("record not found for id - " + str(self.id))

    def findById(self, id):
        with open(self.filePath, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(str(id) + ','):
                    return line.split(',')
            raise ValueNotFound("record not found for id - " + str(self.id))
