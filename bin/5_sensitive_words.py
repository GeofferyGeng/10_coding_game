def st(t, s):
    t = t.replace(s, "**")
    return t


def main():
    text = "五、敏感词审查一向痛恨网络审查的你成了某网站的审查员，要求审查网络上违反上头规定的名词。功能描述：要审查的帖子在这个文本文档里，要求将所有的和谐"
    s = "网络"
    s_text = st(text, s)
    print(s_text)


if __name__ == '__main__':
    main()
