import imaplib
import os
import email
import sys
import json
import requests


class GMAIL_EXTRACTOR():
    def helloWorld(self):
        print("\nWelcome to the Gmail Inbox Analyser")

    def initializeVariables(self):
        self.usr = ""
        self.pwd = ""
        self.mail = object
        self.mailbox = ""
        self.mailCount = 0
        self.destFolder = ""
        self.data = []
        self.ids = []
        self.idsList = []

    def getLogin(self):
        print("\nPlease enter your Gmail login details below.")
        self.usr = input("Email: ")
        self.pwd = input("Password: ")

    def attemptLogin(self):
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        if self.mail.login(self.usr, self.pwd):
            print("\nLogon SUCCESSFUL")
            if not self.destFolder.endswith("/"): self.destFolder += "/"
            return True
        else:
            print("\nLogon FAILED")
            return False

    