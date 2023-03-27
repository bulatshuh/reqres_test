from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_LOGO_BUTTON = (By.CSS_SELECTOR, '[src="/img/logo.png"]')
    G0_TO_SUPPORT_BUTTON = (By.CSS_SELECTOR, '[href="#support-heading"]')
    SUPPORT_BUTTON = (By.CSS_SELECTOR, '.breathe button')
    MONEY_AMOUNT_FIELD = (By.CSS_SELECTOR, '[name="oneTimeAmount"]')
    SEND_REQUEST_BUTTON = (By.CSS_SELECTOR, '.link.try-link')
    RESPONSE_STATUS_CODE_FIELD = (By.CSS_SELECTOR, '.response-code')
    RESPONSE_DATA_FIELD = (By.CSS_SELECTOR, '[data-key="output-response"]')
    SPINNER_IS_HIDDEN = (By.CSS_SELECTOR, '.spinner[hidden="true"]')
    SWAGGER_BUTTON = (By.CSS_SELECTOR, '[src="/img/swagger-logo-horizontal.jpeg"]')
    # request buttons
    LIST_USER_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(1)')
    SINGLE_USER_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(2)')
    SINGLE_USER_NOT_FOUND_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(3)')
    LIST_RESOURCE_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(4)')
    SINGLE_RESOURCE_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(5)')
    SINGLE_RESOURCE_NOT_FOUND_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(6)')
    CREATE_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(7)')
    UPDATE_PUT_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(8)')
    UPDATE_PATCH_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(9)')
    DELETE_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(10)')
    REGISTER_SUCCESSFUL_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(11)')
    REGISTER_UNSUCCESSFUL_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(12)')
    LOGIN_SUCCESSFUL_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(13)')
    LOGIN_UNSUCCESSFUL_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(14)')
    DELAYED_RESPONSE_REQUEST_BUTTON = (By.CSS_SELECTOR, '.endpoints :nth-child(1) :nth-child(15)')


class SupportPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '.CheckoutInput#email')
    CARD_NUMBER_FIELD = (By.CSS_SELECTOR, '.CheckoutInput#cardNumber')
    CARD_EXPIRY_FIELD = (By.CSS_SELECTOR, '.CheckoutInput#cardExpiry')
    CARD_CVC_FIELD = (By.CSS_SELECTOR, '.CheckoutInput#cardCvc')
    CARD_NAME_FIELD = (By.CSS_SELECTOR, '.CheckoutInput#billingName')
    COUNTRY_FIELD = (By.CSS_SELECTOR, '#billingCountry')
    COUNTRY_RUSSIA = (By.CSS_SELECTOR, '#billingCountry :nth-child(174)')
    COUNTRY_CYPRUS = (By.CSS_SELECTOR, '#billingCountry :nth-child(58)')
    WRONG_CARD_INFO_MESSAGE = (By.CSS_SELECTOR,
                               '[style="opacity: 1; height: auto;"] .FieldError [role="alert"]')
    PAY_BUTTON = (By.CSS_SELECTOR, '.SubmitButton-IconContainer')
    POWERED_BY_BUTTON = (By.CSS_SELECTOR, '.Footer-PoweredBy .Link .Text')
    TERMS_BUTTON = (By.CSS_SELECTOR, '.Footer-Links :nth-child(1).Link .Text')
    PRIVACY_BUTTON = (By.CSS_SELECTOR, '.Footer-Links :nth-child(2).Link .Text')
    OPENED_LINK_TITLE = (By.CSS_SELECTOR, '.Copy__title')
    BACK_BUTTON = (By.CSS_SELECTOR, '.InlineSVG.Icon.Header-backArrow.mr2.Icon--sm')

# При вводе почты изначально выходло окно верификации, затем перестало,
# на всякий случай, решил оставить данные, для этого окна -
# закомменчено в locators, support_page, test_support_page:

    # EMAIL_VERIFICATION = (By.CSS_SELECTOR, '.VerificationModal-modalContent')
    # EMAIL_VERIFICATION_CANCEL_BUTTON = (By.CSS_SELECTOR, '.Button.Button--secondary.Button--md.Button--fullWidth')
