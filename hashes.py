#!/usr/bin/env python3
import os, sys, platform, getpass, hashlib
from tkinter import *
from tkinter.ttk import *

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "Hashes") # Set window title
        self.resizable(0,0) # Do not allow to be resized
        self.style = Style()
        self.style.theme_use("clam")
        icon = PhotoImage(file='icon.png') # Set app icon
        self.tk.call('wm', 'iconphoto', self._w, icon) # Call app icon

        # Input field data is being inserted in this dict
        self.options = {
            'file' : StringVar(),
            'hash' : StringVar(),
            'MD5' : StringVar(),
            'SHA1' : StringVar(),
            'SHA256' : StringVar(),
            'SHA384' : StringVar(),
            'SHA512' : StringVar(),
        }

        # Set default values
        if platform.system() == 'Windows':
            self.options['file'].set('C:\\Users\\' + getpass.getuser() + '\\Desktop\\' )
        elif platform.system() == 'Linux':
            self.options['file'].set('/home/' + getpass.getuser() + '/')
        else:
            self.options['file'].set('C:\\Users\\' + getpass.getuser() + '\\Desktop\\' )

        # Label Frame
        settings = LabelFrame(self, text = 'Data', relief = GROOVE, labelanchor = 'nw', width = 440, height = 100)
        settings.grid(row = 0, column = 1)
        settings.grid_propagate(0)

        # File entry
        Label(settings, text = 'File:').grid(row = 0, column = 0)
        Entry(settings, textvariable = self.options['file'], width = 45).grid(row = 0, column = 1, columnspan = 2)

        # Hash entry
        Label(settings, text = 'Hash:').grid(row = 1, column = 0)
        Entry(settings, textvariable = self.options['hash'], width = 45).grid(row = 1, column = 1, columnspan = 2)

        # Select row frame
        encodings = LabelFrame(self, text = 'Encodings', relief = GROOVE, labelanchor = 'nw', width = 440, height = 150)
        encodings.grid(row = 1, column = 1)
        encodings.grid_propagate(0)

        # Hashes entry
        Label(encodings, text = 'MD5:').grid(row = 0, column = 0)
        Entry(encodings, textvariable = self.options['MD5'], width = 45).grid(row = 0, column = 1, columnspan = 2)

        Label(encodings, text = 'SHA1:').grid(row = 1, column = 0)
        Entry(encodings, textvariable = self.options['SHA1'], width = 45).grid(row = 1, column = 1, columnspan = 2)

        Label(encodings, text = 'SHA256:').grid(row = 2, column = 0)
        Entry(encodings, textvariable = self.options['SHA256'], width = 45).grid(row = 2, column = 1, columnspan = 2)

        Label(encodings, text = 'SHA384:').grid(row = 3, column = 0)
        Entry(encodings, textvariable = self.options['SHA384'], width = 45).grid(row = 3, column = 1, columnspan = 2)

        Label(encodings, text = 'SHA512:').grid(row = 4, column = 0)
        Entry(encodings, textvariable = self.options['SHA512'], width = 45).grid(row = 4, column = 1, columnspan = 2)

        # Buttom Buttons frame
        buttons = LabelFrame(self, text = 'Options', relief = GROOVE, labelanchor = 'nw', width = 440, height = 100)
        buttons.grid(row = 2, column = 1)
        buttons.grid_propagate(0)

        # Bottom buttons
        show_hashes = Button(buttons, text = "HASH", command = self.hash_all, width = 53).grid(row = 0, column = 0, columnspan = 3)
        exit_app = Button(buttons, text = "EXIT", command = exit, width = 53).grid(row = 1, column = 0, columnspan = 3)
        
    def decode_base_now(self, event):
        print('Comming Soon!')
        self.enter_val.destroy()

    def hash_all(self):
        hashes = {'md5': self.md5(),
            'sha1': self.sha1(),
            'sha256': self.sha256(),
            'sha384': self.sha384(),
            'sha512': self.sha512(),
            }

        self.options['MD5'].set(self.md5())
        self.options['SHA1'].set(self.sha1())
        self.options['SHA256'].set(self.sha256())
        self.options['SHA384'].set(self.sha384())
        self.options['SHA512'].set(self.sha512())

        # Search a match with given hash
        if self.options['hash'].get():
            for encoding, hash in hashes.items():
                if hash == self.options['hash'].get():
                    print(True)
                    print(encoding)
                    self.title(string = "Hashes - Match Found! Your %s hash matches" % encoding)
                    break
                else:
                    self.title(string = "Hashes - No Match Found!")

    def md5(self):
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(self.options['file'].get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

    def sha1(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha1()
        with open(self.options['file'].get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

    def sha256(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha256()
        with open(self.options['file'].get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

    def sha384(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha384()
        with open(self.options['file'].get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

    def sha512(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha512()
        with open(self.options['file'].get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return hasher.hexdigest()

main = MainWindow()
main.mainloop()
