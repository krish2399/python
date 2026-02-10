class Text(str):
    def duplicate(self):
        return self + self


class TracableList(list):
    def append(self, object):
        print("append is called")
        super().append(object)


list = TracableList()
list.append(10)
print(list)
