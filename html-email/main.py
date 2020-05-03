# TODO: the responsibility of each class should be clear.
from HTMLEmail import HTMLEmail, HTMLEmailBuilder
from builder import rewrite_main


class GenerateHTMLEmail:
    """ Generate HTMLEmail's class. """

    def __init__(self, file_path):
        self.builder = None
        self.file_path = file_path

    def setup(self):
        """
        set up all information of html.
        :return:
        """
        self.builder = HTMLEmailBuilder(self.file_path)

        header_content = input('Please type header content:\n')
        content = input('Please type the content what you want to show in this page.\n')
        foot = input('Please type the content of foot.\n')

        self.builder.config_header(header_content)
        self.builder.config_body(content)
        self.builder.config_foot(foot)
        self.builder.config_html()
        print(self.builder.htmlemail.__str__())

    def create_html_email(self):
        """
        create a html email page: test.html.
        :return:
        """
        try:
            f = open(self.file_path, 'w+')
            f.write(self.builder.htmlemail.html)
            f.close()
        except Exception as e:
            print(f'[Error] create_html_email, {e}')


def main():
    # TODO: user have to type the path of your file.
    path = "D:\\github_project\\side_project_with_py\\html-email\\test.html"
    g = GenerateHTMLEmail(path)
    g.setup()
    g.create_html_email()

    # TODO: improve the builder.
    # TODO: send email to clients.


if __name__ == '__main__':
    """ pick up one what users want. """
    # main()
    rewrite_main()
