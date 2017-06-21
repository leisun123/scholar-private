from ScholarClass import Scholar
import time
class ScholarArticle(Scholar):
    def __init__(self,ScholarObj=None):
        super(ScholarArticle, self).__init__()
        self.ScholarObj=ScholarObj
        self.title=None
        self.url=None
        self.author=None
        self.email=None

    def generate_title(self):
        pass

    def generate_url(self):
        pass

    def generate_author(self):
        pass

    def generate_email(self):
        pass

    def generate_all_method(self):
        self.generate_title()
        self.generate_url()
        self.generate_author()
        self.generate_email()

    def insertdb(self):
        self.conn=self.connectdb()
        self.cur=self.conn.cursor()
        # self.cur.execute(
        #     """
        #     CREATE TABLE scholar
        #     (
        #         title   varchar(200),
        #         url     varchar(200),
        #         author  varchar(50),
        #         email   varchar(100)
        #     )
        #     """
        #
        # )

        self.cur.execute(
            "INSERT INTO scholar(\
                url,\
                title,\
                author,\
                email)\
            VALUES('{}','{}','{}','{}')".format(self.url,self.title, self.author,self.email))
        self.conn.commit()

    def show_in_cmd(self):
        print('******************************************')
        print('url:\t\t{}'.format(self.url))
        print('title:\t\t{}'.format(self.title))
        print('author:\t\t{}'.format(self.author))
        print('email:\t\t{}'.format(self.email))


























