from selenium import webdriver
import pytest
import pytest_html

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    elif browser_name =="firefox":
        driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    else:
        print("IE driver")
    driver.maximize_window()
    return driver

######################PyTest HTML Report #################
#It is hook for Adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester']='Divya'

#It is hook for delete/Modify Environment info HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
