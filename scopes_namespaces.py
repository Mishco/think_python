
class scopeTestClass:
    """A scope testing class

     Namespace"""
    """class variable shared by all instance """
    spam = "testovacia sprava 1"

    def scope_test(self):
        def do_local():
            spam = "lokalny spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nie lokalny spam"

        def do_global():
            global spam
            spam = "Globalna sprava"

        spam = "testovaca sprava"
        do_local()
        print(spam)
        do_nonlocal()
        print(spam)
        do_global()
        print(spam)
