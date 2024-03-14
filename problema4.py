from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

    def handle_comment(self, data):
        pass

if __name__ == "__main__":
    n = int(input().strip())
    html_code = ""
    for _ in range(n):
        html_code += input().strip()

    parser = MyHTMLParser()
    parser.feed(html_code)
