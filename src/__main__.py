from .example import save, load
from .example.default import Article
from .example.complex import Article as ComplexArticle
from .example.reality import SomePage


def main():
    # a = SomePage()
    # # a.ipaddr.value = "192.168.2.0"
    # save(a, path="src/data/reality_output.txt")
    # print(a)

    b = load(SomePage, path="src/data/reality_output.txt")
    print(b)


main()
