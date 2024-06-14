"""
Constants for URL and XPATH elements
"""


class SearchProductConstants:
    URL = 'https://rozetka.com.ua/ua/'
    INPUT_XPATH = '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/div/div[1]/input'


class CheckBasketConstants:
    URL = 'https://rozetka.com.ua/ua/apple-iphone-15-pro-max-512gb-natural-titanium/p395461116/'
    BUTTON_XPATH = '//*[@id="#scrollArea"]/div[1]/div[2]/div/rz-product-main-info/div/div[2]/div[1]/div[3]/rz-product-buy-btn/rz-buy-button/button'
    BASKET_XPATH = '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[8]/rz-header-cart/button'
    BASKET_BTN_XPATH = '/html/body/rz-app-root/rz-single-modal-window/div[3]/div[2]/rz-shopping-cart/div/rz-cart-purchases/ul/li/rz-cart-product/div/div[1]/rz-popup-menu/button'
    BASKET_DELETE_BTN_XPATH = '/html/body/rz-app-root/rz-single-modal-window/div[3]/div[2]/rz-shopping-cart/div/rz-cart-purchases/ul/li/rz-cart-product/div/div[1]/rz-popup-menu/div'
    CHECK_IN_BASKET_MSG_XPATH = '/html/body/rz-app-root/rz-single-modal-window/div[3]/div[2]/rz-shopping-cart/div/div[1]/h4'
    CHECK_BASKET_XPATH = '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[8]/rz-header-cart/button/rz-icon-badge/span'
