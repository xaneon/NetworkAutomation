class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attr = getattr(self, key)
            attrs.append('%s=%s' % (key, attr))
        return ', '.join(attrs)
    def __repr__(self):
        clsName = self.__class__.__name__
        clsAttrs = self.gatherAttrs()
        return '[%s: %s]' %(clsName, clsAttrs)

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()
    K, L = TopTest(), SubTest()
    print(X)
    print(Y)
    print(K)
    print(L)
