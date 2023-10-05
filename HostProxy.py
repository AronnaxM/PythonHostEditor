#Host Proxy
'''Please Run "pip install python-hosts
"Before Run'''
from python_hosts import Hosts, HostsEntry
hosts = Hosts(path='C:\Windows\System32\drivers\etc')    #Locate Host File
UserNames=input('Input Address').split(',')
SiteNames=input('Site Names').split(',')
AllItems=dict(zip(UserNames,SiteNames))
for un,sn in AllItems.items():
    user_entry = HostsEntry(entry_type='ipv4', address='127.0.0.1', names=[un, sn])
hosts.add([user_entry])
hosts.write()
#Add Comments
NewComment1 = HostsEntry(entry_type='comment', comment='# an example comment')
hosts.add(entries=[NewComment1], force=True)
hosts.write()