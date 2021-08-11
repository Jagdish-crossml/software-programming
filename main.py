class Lists():

    def __init__(self, name):
        self.name = name

    def read_list(self, file_name):
        with open(file_name, 'r') as f:
            lst = f.readlines()

        return lst


reed = Lists(123)
# print(reed.read_list('file1.txt'))
l = reed.read_list('file1.txt')
with open('new.txt','w') as j:
    for i in l:
        j.write(i)



