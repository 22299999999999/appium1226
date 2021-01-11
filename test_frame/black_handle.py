import logging

import allure

logging.basicConfig(level=logging.INFO)


def black_wrapper(fun):
    def run(*args, **kwargs):
        first = args[0]
        try:
            logging.info("start find : \nargs: " + str(args) + " kwargs: " + str(kwargs))
            return fun(*args, **kwargs)
        except Exception as e:
            first.screenshot('./tmp.png')
            with open('./tmp.png', 'rb') as f:
                picture = f.read()
            allure.attach(picture, attachment_type=allure.attachment_type.PNG)

            for black in first.black_list:
                elements = first.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return fun(*args, **kwargs)
        raise e

    return run
