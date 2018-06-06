# Why? #
When I think of something, I want to open a script that lets me enter a task and due date very quickly without having to open a browser to Wunderlist. I will organize into the correct folder later.

# Get Wunderpy2
* More info on wunderpy2: https://github.com/mieubrisse/wunderpy2

Get the wunderpy2 package using pip:
```
pip install wunderpy2
```

# Requirements
  This example has been tested with Python 3.6.4, but with the following changes:

in `site-packages\wunderpy2\tasks_endpoint.py` (line 54), replace `iteritems()` with `items()`  ; See: https://github.com/mieubrisse/wunderpy2/pull/7


# Get access_token and client_id
1. Go to http://developer.wunderlist.com
2. Register
3. Create an App
   * App URL: http://localhost
   * Auth Callback URL: http://localhost
4. Once the App is created, Create Access Token
5. Create a file called myconfig.py (in the same folder/dir as this README)
   * Note: *access_token and client_id are enclosed in single quotes because they are long strings; list_id will be a number*

```
access_token = 'YOUR_ACCESS_TOKEN_FROM_STEP4'
client_id = 'YOUR_CLIENT_ID_FROM_STEP3'
list_id = LOOK_BELOW
```

# Want to get the ID of your Inbox?
All new lists you create in *Wunderlist* will have the ID at the end of the URL (when you are in a browser looking at your Wunderlist List). The ID of the Inbox is hard to get.
```
python get_inbox_id.py
```
This will print the ID of your Inbox. 


Place the list ID of the list you want to add tasks to in the file **myconfig.py** for the parameter **list_id**

# Add a Task
```
python me_wunder.py
```
2 prompts will come up.
1. Enter the task: *Enter your task description*
2. Days from now (optional YYYY-MM-DD): 
   * just hit enter and **NO** due date will be set
   * OR Enter the days from now (for example: 5)
   * OR a specific date in the format YYYY-MM-DD (for example: 2019-01-01)
