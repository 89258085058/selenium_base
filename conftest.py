# -*- coding: utf-8 -*-

import json
import logging
import os.path

import pytest

from base.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture(scope='class')
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]
    fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.main_page.goToMainPage()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="chrome")
    parser.addoption("--target", action='store', default="target.json")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    result = yield
    report = result.get_result()
    if report.longrepr:
        logging.error('FAILED: %s', report.longrepr)
    else:
        logging.info('Did not fail...')
    if report.outcome == 'failed':
        fixture.get_screen()
        logging.error('FAILED: %s', report.longrepr)
    elif report.outcome == 'skipped':
        logging.info('Skipped')
    else:
        logging.info('Passed')
