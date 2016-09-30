from behave import *

from accounts.factories import InterestFactory

from accounts.factories import UserFactory
from accounts.models import Interest


@given('there are a number of interests')
def impl(context):
    interests = [InterestFactory(name=row['interest']) for row in context.table]


@given('there are many users, each with different interests')
def impl(context):
    for row in context.table:
        interest_names = row['interests'].split(', ')
        interests = Interest.objects.filter(name__in=interest_names)
        UserFactory(email=row['email'], interests=interests)


@given('I am a logged un user')
def impl(context):
    user_to_login = UserFactory(email='log.me.in@test.test')
    context.browser.visit(context.config.server_url + 'accounts/login/')

    context.browser.fill('username', user_to_login.email)
    context.browser.fill('password', 'pass')

    context.browser.find_by_css('form input[type=submit]').first.click()


@when('I filter the list of users by "{checked}"')
def impl(context, checked):
    context.browser.visit(context.condif.server_url)

    checked = checked.split(', ');
    for check in checked:
        path = "//label[contains(.,'{}')]/input".format(check)
        context.browser.find_by_xpath(path).click()
    context.browser.find_by_css('form input[type=submit]').first.click()


@then('I see "{count}" users')
def impl(context, count):
    users = context.browser.find_by_css('.user-card')

    assert len(users) == int(count)


