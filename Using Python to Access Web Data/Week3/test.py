#!/:wqusr/bin/python3

import re
'''
1. 

What do we call it when a browser uses the HTTP protocol to load a file or page from a server and display it in the browser?

The Request/Response Cycle

DECNET

SMTP

IMAP

Internet Protocol (IP)
2. 

What separates the HTTP headers from the body of the HTTP document?

X-End-Header: true

A blank line

Four dashes

A less-than sign indicating the start of an HTML tag
3. 

What must you do in Python before opening a socket?

_socket = true

import socket

import tcp

import tcp-socket

open socket
4. 

Which of the following TCP sockets is most commonly used for the web protocol (HTTP)?

23

22

80

25

119
5. 

Which of the following is most like an open socket in an application?

An "in-progress" phone conversation

Fiber optic cables

The wheels on an automobile

The chain on a bicycle

The ringer on a telephone
6. 

What does the "H" of HTTP stand for?

Manual

HyperText

Simple

wHolsitic

Hyperspeed
7. 

What is an important aspect of an Application Layer protocol like HTTP?

What is the IP address for a domain like www.dr-chuck.com?

How long do we wait before packets are retransmitted?

Which application talks first? The client or server?

How much memory does the server need to serve requests?
8. 

What are the three parts of this URL (Uniform Resource Locator)?

http://www.dr-chuck.com/page1.htm

Protocol, host, and document

Document, page, and protocol

Host, offset, and page

Page, offset, and count

Protocol, document, and offset
9. 

When you click on an anchor tag in a web page like below, what HTTP request is sent to the server?

<p>Please click <a href="page1.htm">here</a>.</p>

GET

POST

PUT

DELETE

INFO
10. 

Which organization publishes Internet Protocol Standards?

SIFA

IETF

LDAP

SCORM

IMS
'''
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print("Question 8:")
print(y)

'''
Question 10
'''
str10 = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
found10 =  re.findall('\S+?@\S+', str1)
print("Question 10:")
print(found10)


