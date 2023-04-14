## 1. I hide the current/remote location option before user pass the authentication process.

## 2. under the weather info, the conditon icon does not work over http and https, so i replaced it with the text. 
	(I tried 'condition_icon': data['current']['condition']['icon'],'condition_icon': f"https:{data['current']['condition']['icon']}" in views.py) 
	and (<p>Condition: <img src="{{ location_data.condition_icon }}" alt="Weather Condition Icon" width="64" height="64"></p> in html)
	I can see the url is correct and display img on my brower but not in my django project.
## 3. I use "ip_address, _ = get_client_ip(request)" to get client ip address, but when in test environment, I mannually assigned an IP address to the code.
## 4.The credentials for access is:
##       UserName: YongjiChen
##       Password: 400168246
##	     OR can run command  python manage.py createsuperuser   in terminal to register.