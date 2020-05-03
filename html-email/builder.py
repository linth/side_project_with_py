

class HTMLEmailBuilder:
    """ The builder of HTML Email class. """

    def __init__(self):
        self.file_path = ""
        self.html = ""
        self.header = ""
        self.body = ""
        self.foot = ""

    def config_file_path(self, file_path):
        self.file_path = file_path
        return self

    def config_html(self):
        self.html = "<html>" + self.header + self.body + self.foot + "</html>"
        return self

    def config_header(self, header):
        self.header = "<header>" + header + "</header>"
        return self

    def config_body(self, body):
        self.body = "<body>" + body + "</body>"
        return self

    def config_foot(self, foot):
        self.foot = "<footer>" + foot + "</footer>"
        return self

    def config_css(self):
        return self

    def config_js(self):
        return self


class GenerateHTMLEmail:
    """ Generate HTMLEmail's class. """

    def __init__(self, builder):
        self.file_path = builder.file_path
        self.html = builder.html
        self.header = builder.header
        self.body = builder.body
        self.foot = builder.foot

    def create_html_email(self):
        """
        create a html email page: test.html.
        :return:
        """
        try:
            f = open(self.file_path, 'w+')
            f.write(self.html)
            f.close()
        except Exception as e:
            print(f'[Error] create_html_email, {e}')


def main():
    # TODO: user have to type the path of your file.
    path = "D:\\github_project\\side_project_with_py\\html-email\\test.html"

    builder = HTMLEmailBuilder()\
        .config_file_path(path)\
        .config_header(input('Please type header content:\n'))\
        .config_body(input('Please type the content what you want to show in this page.\n'))\
        .config_foot(input('Please type the content of foot.\n'))\
        .config_html()

    g = GenerateHTMLEmail(builder)
    g.create_html_email()


if __name__ == '__main__':
    main()