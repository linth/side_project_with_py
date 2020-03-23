class HTMLEmail:
    """ HTML Email class. """

    def __init__(self):
        self.file_name = 'test.html'
        self.html = None
        self.header = None
        self.body = None
        self.foot = None

    def __str__(self):
        """
        show HTML Email's information.
        :return: HTML Email's information.
        """
        return f'the HTML: {self.file_name} is generated ' \
               f'The content of HTML is including: ' \
               f'html: {self.html}' \
               f'body: {self.body} ' \
               f'foot: {self.foot}'


class HTMLEmailBuilder:
    """ The builder of HTML Email class. """

    def __init__(self, file_path):
        self.file_path = file_path
        self.htmlemail = HTMLEmail()

    def config_html(self, html):
        """
        set up the html part.
        :param html:
        :return:
        """
        self.htmlemail.html = html

    def config_header(self, header):
        """
        set up the header part.
        :param header:
        :return:
        """
        self.htmlemail.header = header

    def config_body(self, body):
        """
        set up the body part.
        :param body:
        :return:
        """
        self.htmlemail.body = body

    def config_foot(self, foot):
        """
        set up the foot part.
        :param foot:
        :return:
        """
        self.htmlemail.foot = foot

    def config_css(self):
        pass

    def config_js(self):
        pass

