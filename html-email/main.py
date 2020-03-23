from HTMLEmail import HTMLEmail, HTMLEmailBuilder


class GenerateHTMLEmail:

    def __init__(self, file_path):
        self.builder = None
        self.file_path = file_path
        self.all = None # all content.

    def setup(self):
        self.builder = HTMLEmailBuilder(self.file_path)

        foot = "<foot></foot>"
        header_content = input('Please type header content:\n')
        content = input('Please type what you want to show in this page.\n')

        header = "<head>" + header_content + "</head>"
        body = "<body>" + content + "</body>"
        html = "<html>" + header + body + "</html>"

        self.builder.config_html(html)
        self.builder.config_header(header)
        self.builder.config_body(body)
        self.builder.config_foot(foot)
        print(self.builder.htmlemail.__str__())
        self.all = html

    def create_html_email(self):
        """
        create a html email page: test.html.
        :return:
        """
        try:
            f = open(self.file_path, 'w+')
            f.write(self.all)
            f.close()
        except Exception as e:
            print(f'[Error] create_html_email, {e}')


def main():
    # TODO: user have to type the path of your file.
    path = "D:\\github_project\\side-project\\html-email\\test.html"
    g = GenerateHTMLEmail(path)
    g.setup()
    g.create_html_email()


if __name__ == '__main__':
    main()
