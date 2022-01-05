# Import pyshorteners module
import pyshorteners

print('Shortens a long URl to a tiny one')

userurl = input('Please type in the URL to shorten: ')

shorturl = pyshorteners.Shortener().tinyurl.short(userurl)

print(shorturl)
