from behave import *
from splinter.browser import Browser
from django.core import management


def before_all(context):
    if context.config.browser:
        context.browser = Browser(context.config.browser)
    else:
        context.browser = Browser('phantomjs')

    if context.browser.driver_name == 'PhantomJS':
        context.browser.driver.set_window_size(1280, 1024)


def before_scenario(context, scenario):
    management.call_command('flush', verbosity=0, interactive=False)


def after_all(context):
    context.browser.quit()
    context.browser = None
