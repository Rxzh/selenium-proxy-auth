# Python Selenium with proxy
The purpose of this repository is to list the method to run a Selenium driver on Python using Proxies servers.

### Authenticated Proxy


```python
from Proxy import init_chrome_options_with_proxy
from selenium import webdriver
```


```python
PROXY_IP       = "192.168.1.1" 
PROXY_PORT     = 80
PROXY_USERNAME ='username'
PROXY_PASSWORD ='pass'

chrome_options = init_chrome_options_with_proxy(PROXY_IP,PROXY_PORT,PROXY_USERNAME,PROXY_PASSWORD)

driver = webdriver.Chrome(chrome_options=chrome_options)
```

### Regular Proxy


```python
#todo
```
