from file_util import FileUtil
from exception import ValueNotFound
from abc import ABC, abstractmethod

class CrudFileRepository(ABC):

    @abstractmethod
    def filepath(self):
        raise NotImplementedError('provide implementation for filepath()')

    def save(self):
        with open(self.filepath(), 'r+') as file:
            lines = file.readlines()
            if self.id is None:
                self.id = 1 if len(lines) is 0 else (int(lines[len(lines) - 1].split(',')[0])) + 1
                file.write((','.join(map(str, self.__dict__.values())) + '\n'))
            else:
                file.truncate(0)
                file.seek(0)
                for line in lines:
                    if line.startswith(str(self.id) + ','):
                        file.write((','.join(map(str, self.__dict__.values())) + '\n'))
                    else:
                        file.write(line)
                raise ValueNotFound("record not found for id - " + str(self.id))

    def find_all(self):
        fileContent = []
        with open(self.filepath(), "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                fileContent.append(line.split(','))
        return fileContent    


    def delete_by_id(self, id):
        with open(self.filepath(), "r+") as file:
            lines = file.readlines()
            file.truncate(0)
            file.seek(0)
            for lineNumber, line in enumerate(lines[:]):
                if not line.startswith(str(id) + ','):
                    file.write(line)
            raise ValueNotFound("record not found for id - " + str(id))

    def find_by_id(self, id):
        with open(self.filepath(), "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
                if line.startswith(str(id) + ','):
                    return line
            raise ValueNotFound("record not found for id - " + str(id))
