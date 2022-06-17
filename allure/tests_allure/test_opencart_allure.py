import allure
from OTUS.allure.page_objects_allure.CatalogPage_allure import CatalogPage
from OTUS.allure.page_objects_allure.MainPage_allure import MainPage


class TestOpencart:

    @allure.title("Elements on main page")
    def test_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.open_page()
        assert main_page.count_heading_links() == 7
        logo = main_page.shop_logo()
        assert logo.get_attribute("title") == "Your Store"
        search_placeholder = main_page.search_placeholder()
        assert search_placeholder == "Search"

    @allure.title("Change currency om main page")
    def test_switch_currency(self, browser):
        main_page = MainPage(browser)
        main_page.open_page()
        main_page.change_currency("EUR")
        assert main_page.CURRENCY["EUR"] == main_page.current_sign_currency

    @allure.title("Elements on catalog page")
    def test_catalog_page(self, browser):
        catalog_page = CatalogPage(browser)
        catalog_page.open_laptop_page()
        assert browser.title == "Laptops & Notebooks"
        assert catalog_page.count_product_cards == 5
        catalog_page.sort_products_by("Price (High > Low)")
        assert catalog_page.get_current_sort_filter == "Price (High > Low)"

