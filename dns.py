#!/usr/bin/env python3

import dns.resolver
import pandas as pd
import csv

#domain: FQDN & rtype 'A' or 'AAAA'
def dns_lookup(domain,rtype):
    try:
        # Resolve the record type (A or AAAA  for the FQDN in 'domain'
        result = dns.resolver.resolve(domain, rtype)
        for ip in result:
#            print(f'{domain} resolves to {ip.address}')
            return (ip.address)
    except dns.resolver.NoAnswer:
 #       print(f'No record found for {domain}')
        return ("No record")
    except dns.exception.DNSException as e:
  #      print(f'DNS lookup failed: {e}')
        return ("DNS query failed")

# Pandas reading csv file
df = pd.read_csv("/home/nacho/Documents/projects/python/FQDNs.csv")

for index, row in df.iterrows():
    test=df.loc[index,'fqdn']
    A=dns_lookup(test,'A')
    AAAA=dns_lookup(test,'AAAA')

    df.loc[index,'a'] = A
    df.loc[index,'aaaa'] = AAAA
    print (df.loc[index])
    #
#Pandas store DataFrame to CSV
df.to_csv("/home/nacho/Documents/projects/python/processed.csv")
