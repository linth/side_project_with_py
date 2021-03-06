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

    def config_html(self):
        """
        set up the html part.
        :param html: add the <html></html> part.
        :return:
        """
        self.htmlemail.html = "<html>" + \
                              self.htmlemail.header + \
                              self.htmlemail.body + \
                              self.htmlemail.foot + \
                              "</html>"

    def config_header(self, header):
        """
        set up the header part.
        :param header: add the <header></header> part.
        :return:
        """
        self.htmlemail.header = "<header>" + header + "</header>"

    def config_body(self, body):
        """
        set up the body part.
        :param body: add the <body></body> part.
        :return:
        """
        self.htmlemail.body = "<body>" + body + "</body>"

    def config_foot(self, foot):
        """
        set up the foot part.
        :param foot: add the <footer></footer> part.
        :return:
        """
        self.htmlemail.foot = "<footer>" + foot + "</footer>"

    def config_css(self):
        pass

    def config_js(self):
        pass

