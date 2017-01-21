class Repository:
    def __init__(self, file_name):
        """
        :param file_name: String
        """
        self.__file_name = file_name
        self.__attr = []
        self.__load_from_file()

    def __write_to_file(self):
        f = open(self.__file_name, 'w')
        f.write(self.__attr)
        f.close()

    def __load_from_file(self):
        """
        :raises IOError, IndexError
        :raise IOError: if the file didn't find or can't open
        :raise IndexError: if the file is corrupt
        """
        try:
            f = open(self.__file_name, 'r')
            line = f.readline()
            self.__attr = line.split(';')
            f.close()
        except IOError:
            raise IOError("The file didn't find or can't open!")
        except IndexError:
            raise IndexError('Encountering an error while read the file!')

    def get_param(self):
        """
        :return  a copy of self.__attr: list
        """
        return self.__attr[:]

    def save(self, attr):
        """
        :param attr: String
        """
        self.__attr = attr
        self.__write_to_file()
