import hashlib



sha1 = hashlib.sha1(b"https://www.iana.org/_img/2013.1/iana-logo-header.svg").hexdigest()   

print(sha1)
