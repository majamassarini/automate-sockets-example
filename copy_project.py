import pywebcopy

url = "http://172.31.10.248:8181"
kwargs = {'project_name': 'sockets'}

payload = {'username': "admin", 'password': "admin"}
pywebcopy.SESSION.post("{}/login".format(url), data=payload)

pywebcopy.save_website(
    url=url,
    project_folder='.',
    **kwargs
)
