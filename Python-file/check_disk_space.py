import shutil

du =shutil.disk_usage('/')

print(du)
free_percent = (du.free/ du.total)*100
used_prercent =(du.used/du.total)*100


print(f'Free disk:{round(free_percent,2)}% ')
print(f'Used disk:{round(used_prercent,2)}% ')