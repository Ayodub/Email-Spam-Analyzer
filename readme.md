Requirements:

This email verification program requires a number of python libraries. The following libraries are external and will require the user to install them:

imaplib
Email
requests
colorama (optional, for colored text output).

Once the per-requisite installs are complete, the program can be ran by navigating through terminal to it's downloaded location and typing: python3 main.py

At this point a welcome message should appear, and the user will be prompted to enter their Gmail credentials. Upon first login it is possible that the user may be required to allow this app access. An email will be sent to the user's gmail account asking if they would like to allow a security exception for this app. If this message is sent the user must accept the exception in order to continue with the app. After allowing this exception they can again attempt to sign in to the app.

Upon successful login, the user will be asked to specify a Gmail directory to scan. This may include Inbox, drafts, trash, or any other directory they have on their Gmail dashboard. The email verification app will then proceed through all of their emails extracting headers and email addresses in order to assess them based on DNS records, SMTP pings and more. A score will be returned along with a message advising how likely the email is to be spam.
