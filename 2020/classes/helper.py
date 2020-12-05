class Helper:

    def read_file(file_name):
        f = open(file_name, 'r')
        my_file_data = f.read()
        f.close()
        return my_file_data
