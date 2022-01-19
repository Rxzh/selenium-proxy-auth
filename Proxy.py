import zipfile
import os
from selenium import webdriver

def set_manifest():
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    return manifest_json

def set_background(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):
    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

    return background_js


def BrowserInit(PROXY_HOST="8080.8080.8080.8080", 
                PROXY_PORT=80, 
                PROXY_USER='username', 
                PROXY_PASS='password'):
    chrome_options = webdriver.ChromeOptions()
    pluginfile = 'proxy_auth.zip'
    manifest_json = set_manifest()
    background_js = set_background(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    chrome_options.add_extension(pluginfile)
    os.remove(os.path.abspath(pluginfile))
    webdriver.Chrome(chrome_options=chrome_options)
