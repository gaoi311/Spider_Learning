from lxml import etree

if __name__ == '__main__':
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("test.html", parser=parser)
    # r = tree.xpath("//div[@class='song']")
    # r = tree.xpath('/html/head/title')
    # r = tree.xpath("//div[@class='song']/p[3]")
    # r = tree.xpath("//div[@class='tang']//li[4]/a/text()")
    r = tree.xpath("//div[@class='song']//@src")
    print(r)