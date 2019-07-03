from selector_main import SelectorMain
from selector_api import SelectorApi

main_page = SelectorMain()

main_page.login()

main_page.load_report_open("МАДИ")

main_page.select_report_period()

main_page.switch_to_report_window()

report_id = main_page.get_report_id()
print(report_id)

report_period = main_page.convert_date()
print(report_period)

main_page.confirm_report()





