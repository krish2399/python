class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, __tag):
        self.tags[__tag.lower()] = self.tags.get(__tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.ger(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        len(self.tags)

    def __iter__(self):
        iter(self.tags)


cloud = TagCloud()
cloud["Python"] = 10
print(len(cloud))
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)
