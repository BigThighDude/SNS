#this file is used to populate data fields in the dns dictionary, and is imported into the main file
#for simplicity, only one nameserver, one mx server, and only ipv4 formats are used

#nslookup = nameserver lookup
#types of dns records:
#NS = name server format:server:routerip, address:localip, non-auth answer: web address _ nameserver = ns...com, ns....com internetaddress = ipv4, ns....com internetaddress = ipv6
#MX = mail server format:server:routerip, address:localip, non-auth answer: web address _ mx preference = int, mail exchanger = web.host.com
#SOA = store admin information format: server:routerip, address:localip, non-auth answer: web address, primary name server=ns...com, responsible mail addr = x.web.com,



localip = '192.168.0.x' #this depends on the device local ip with respect to the router; remains same regardless of dns query

dnsq = {}   #create dictionary within which dictionaries for each website will be nested


dnsq['ucl'] = {}    #create dictionary for ucl website; data for each field is already populated as in a dns lookup server

dnsq['ucl']['webad'] = 'ucl.ac.uk'  #domain web address
dnsq['ucl']['ip'] = '144.82.250.24' #ip of web address
dnsq['ucl']['ns'] = 'dns-ns0.ucl.ac.uk' #nameserver
dnsq['ucl']['nsad'] = '193.60.252.2'    #ip of the nameserver
dnsq['ucl']['mxp'] = '0'    #this is the priority of a mailserver if there are multiple servers in case one stops working
dnsq['ucl']['mailex'] = 'ucl-ac-uk.mail.protection.outlook.com' #this is the email server
dnsq['ucl']['pns'] = 'dns-ns0.ucl.ac.uk'    #selects the primary nameserver if there are multiple in case one stops working
dnsq['ucl']['rma'] = 'systems.ucl.ac.uk'    #this is the responsible main address - the contact point of the server manager
dnsq['ucl']['serial'] = '2020102801'    #serial number of the domain
dnsq['ucl']['timings'] = 'x hours'  #this normally includes multiple timings for refresh, retry, expire, default TTL etc. for server interaction


dnsq['google'] = {} #same done for google and below for wikipedia

dnsq['google']['webad'] = 'google.co.uk'
dnsq['google']['ip'] = '216.58.212.227'
dnsq['google']['ns'] = 'ns1.google.com'
dnsq['google']['nsad'] = '216.239.32.10'
dnsq['google']['mxp'] = '10'
dnsq['google']['mailex'] = 'aspmx.1.google.com'
dnsq['google']['pns'] = 'ns1.google.com'
dnsq['google']['rma'] = 'dns-admin.google.com'
dnsq['google']['serial'] = '339212896'
dnsq['google']['timings'] = 'x hours'


dnsq['wiki'] = {}

dnsq['wiki']['webad'] = 'wikipedia.org'
dnsq['wiki']['ip'] = '91.198.174.192'
dnsq['wiki']['ns'] = 'ns0.wikimedia.org'
dnsq['wiki']['nsad'] = '208.80.154.238'
dnsq['wiki']['mxp'] = '10'
dnsq['wiki']['mailex'] = 'mx1001.wikimedia.org'
dnsq['wiki']['pns'] = 'ns0.wikimedia.org'
dnsq['wiki']['rma'] = 'hostmaster.wikimedia.org'
dnsq['wiki']['serial'] = '2020091413'
dnsq['wiki']['timings'] = 'x hours'

dnsq['defs'] = {} #fields populated for definitions to print before data ie. 'Mail Exchanger'

dnsq['defs']['webad'] = ''
dnsq['defs']['ip'] = 'ip'
dnsq['defs']['ns'] = 'nameserver='
dnsq['defs']['nsad'] = 'internet address='
dnsq['defs']['mxp'] = 'MX preference='
dnsq['defs']['mailex'] = 'mail exchanger='
dnsq['defs']['pns'] = 'primary name server='
dnsq['defs']['rma'] = 'responsible mail address='
dnsq['defs']['serial'] = 'serial='
dnsq['defs']['timings'] = 'refresh='