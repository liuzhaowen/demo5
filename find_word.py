"""
用你擅长的语言将一个文本中出现次数最多的单词找出来. 文本中的单词以空格分隔.
"""


urldir = "./file.txt"

def find_word(urldir):
    words_count = {}
    numTen = []
    # 先文档变成一个字典
    f = open(urldir, 'r')
    for line in f.readlines():
        # 去掉非字符的符号
        # line = re.sub('\W', " ", line)
        lineone = line.strip("/r/n").split(" ")
        for keyone in lineone:
            if not words_count.get(keyone):
                words_count[keyone] = 1
            else:
                words_count[keyone] += 1
        f.close()

    # 整理前10出现的单词的次数
    max_word_count = 0
    for v in words_count.values():
        if v > max_word_count:
            max_word_count = v
        else:
            continue

    for word, v in words_count.items():
        if max_word_count==v:
            print(word, v)
            return word

if __name__ == '__main__':
    find_word(urldir)

