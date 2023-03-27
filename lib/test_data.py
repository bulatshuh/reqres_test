from pages.locators import SupportPageLocators


class TestData:
    number_of_users = [2, 4, 8, 16]

    list_of_correct_ids = [2, 4, 6, 8]

    list_of_incorrect_ids = [23, 44, 56]

    number_of_delays = [2, 3, 4]

    create_user_data = {
        "name": "morpheus",
        "job": "leader"
    }

    update_user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    list_login_user_correct_data = [
        {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        },
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    ]

    login_user_without_password_data = {
        "email": "peter@klaven"
    }

    list_login_user_without_password_data = [
        {
            'email': 'peter@klaven'
        },
        {
            'email': 'eve.holt@reqres.in'
        },
        {
            'email': 'charles.morris@reqres.in'
        }
    ]

    list_login_user_without_email_data = [
        {
            "password": "cityslicka"
        },
        {
            "name": "morpheus",
            "job": "zion resident"
        },
        {

        }
    ]

    list_of_web_request_type_get = [
        {
            'url_for_api': 'api/users?page=2',
            'request_name': 'list users'
        },
        {
            'url_for_api': 'api/users/2',
            'request_name': 'single user'
        },
        {
            'url_for_api': 'api/users/23',
            'request_name': 'single user not found'
        },
        {
            'url_for_api': 'api/unknown',
            'request_name': 'list resource'
        },
        {
            'url_for_api': 'api/unknown/2',
            'request_name': 'single resource'
        },
        {
            'url_for_api': 'api/unknown/23',
            'request_name': 'single resource not found'
        },
        {
            'url_for_api': 'api/users?delay=3',
            'request_name': 'delayed_response'
        }
    ]

    list_of_web_request_type_post = [
        {
            'url_for_api': 'api/users',
            'request_name': 'create',
            'data': create_user_data
        },
        {
            'url_for_api': 'api/register',
            'request_name': 'register_successful',
            'data': list_login_user_correct_data[1]
        },
        {
            'url_for_api': 'api/register',
            'request_name': 'register_unsuccessful',
            'data': login_user_without_password_data
        },
        {
            'url_for_api': 'api/login',
            'request_name': 'login_successful',
            'data': list_login_user_correct_data[1]
        },
        {
            'url_for_api': 'api/login',
            'request_name': 'login_unsuccessful',
            'data': login_user_without_password_data
        },

    ]

    list_of_web_request_type_put = [
        {
            'url_for_api': 'api/users/2',
            'request_name': 'update put',
            'data': update_user_data
        }
    ]

    list_of_web_request_type_patch = [
        {
            'url_for_api': 'api/users/2',
            'request_name': 'update patch',
            'data': update_user_data
        }
    ]

    list_of_web_request_type_delete = [
        {
            'url_for_api': 'api/users/2',
            'request_name': 'delete'
        }
    ]

    list_of_conditions_for_wrong_card_data = ['invalid number', 'past expiry', 'incomplete number']

    list_powered_text = [*SupportPageLocators.POWERED_BY_BUTTON]
    list_terms_text = [*SupportPageLocators.TERMS_BUTTON]
    list_privacy_text = [*SupportPageLocators.PRIVACY_BUTTON]
    list_opened_link_title = [*SupportPageLocators.OPENED_LINK_TITLE]

    list_for_footer_links = [
        {
            'how_link': list_powered_text[0],
            'what_link': list_powered_text[1],
            'expected_text': 'Powered by Stripe',
            'opened_how': list_opened_link_title[0],
            'opened_what': list_opened_link_title[1]
        },
        {
            'how_link': list_terms_text[0],
            'what_link': list_terms_text[1],
            'expected_text': 'Terms',
            'opened_how': list_opened_link_title[0],
            'opened_what': list_opened_link_title[1]
        },
        {
            'how_link': list_privacy_text[0],
            'what_link': list_privacy_text[1],
            'expected_text': 'Privacy',
            'opened_how': list_opened_link_title[0],
            'opened_what': list_opened_link_title[1]
        }
    ]
