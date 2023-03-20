from browser import Browser
from pages.sign_up_page import Sign_up_page
from pages.sign_in_page import Sign_in

def before_all(context):
    #  * beefore_all este o metoda recunoscuta de libraria behave si care se
    #  va executa inainte de toate testele
    #  * context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser()
    context.sign_up_object = Sign_up_page()
    context.sign_in_object = Sign_in()


def after_all(context):
    # * after_all este o metoda recunoscuta de libraria behave si care se
    #     #  va executa dupa de toate testele
    context.browser.close()
