banned_users = ['scott', 'bob', 'carl', 'miguel' ]
authorized_users = {'jeff', 'jam jam', 'carrie underwood'}


for user in authorized_users:
	print(user.title() + ", you can post a response if you wish.")
	
for idx, user in enumerate(banned_users):
	print(user.title() + ", you do not have permissions to post a response on this page.")
	print("You must be a bum.") if idx == 0 else print("You must also be a bum.")
	
