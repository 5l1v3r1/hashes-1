#!/usr/bin/env python3
import os, sys, platform, getpass, hashlib
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename # Import filedialog

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "Hashes") # Set window title
        self.resizable(0,0) # Do not allow to be resized
        self.style = Style() # Enable themes
        self.style.theme_use("clam") # Theme name
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

            'en_md5' : IntVar(),
            'en_sha1' : IntVar(),
            'en_sha256' : IntVar(),
            'en_sha384' : IntVar(),
            'en_sha512' : IntVar(),
        }

        self.bind("<Escape>", self.exit) # Press ESC to quit app

        # Set default values
        if platform.system() == 'Windows':
            self.options['file'].set('C:\\Users\\' + getpass.getuser() + '\\Desktop\\' )
        elif platform.system() == 'Linux':
            self.options['file'].set('/home/' + getpass.getuser() + '/')
        else:
            self.options['file'].set('C:\\Users\\' + getpass.getuser() + '\\Desktop\\' )

        self.options['en_sha1'].set(1)
        self.options['en_sha256'].set(1)

        # Label Frame
        settings = LabelFrame(self, text = 'Data', relief = GROOVE, labelanchor = 'nw', width = 440, height = 100)
        settings.grid(row = 0, column = 1)
        settings.grid_propagate(0)

        # File entry
        Label(settings, text = 'File:').grid(row = 0, column = 0)
        Entry(settings, textvariable = self.options['file'], width = 45).grid(row = 0, column = 1, columnspan = 2)
        select_file = Button(settings, text = '...', command = self.file_browser, width = 2).grid(row = 0, column = 3)

        # Hash entry
        Label(settings, text = 'Hash:').grid(row = 1, column = 0)
        Entry(settings, textvariable = self.options['hash'], width = 45).grid(row = 1, column = 1, columnspan = 2)

        # Select row frame
        encodings = LabelFrame(self, text = 'Encodings', relief = GROOVE, labelanchor = 'nw', width = 440, height = 150)
        encodings.grid(row = 1, column = 1)
        encodings.grid_propagate(0)

        # Hashes entry
        #Label(encodings, text = 'MD5:').grid(row = 0, column = 0)
        Checkbutton(encodings, text="MD5", variable=self.options['en_md5']).grid(row = 0, column = 0)
        Entry(encodings, textvariable = self.options['MD5'], width = 45).grid(row = 0, column = 1, columnspan = 2)

        #Label(encodings, text = 'SHA1:').grid(row = 1, column = 0)
        Checkbutton(encodings, text="SHA1", variable=self.options['en_sha1']).grid(row = 1, column = 0)
        Entry(encodings, textvariable = self.options['SHA1'], width = 45).grid(row = 1, column = 1, columnspan = 2)

        #Label(encodings, text = 'SHA256:').grid(row = 2, column = 0)
        Checkbutton(encodings, text="SHA256", variable=self.options['en_sha256']).grid(row = 2, column = 0)
        Entry(encodings, textvariable = self.options['SHA256'], width = 45).grid(row = 2, column = 1, columnspan = 2)

        #Label(encodings, text = 'SHA384:').grid(row = 3, column = 0)
        Checkbutton(encodings, text="SHA384", variable=self.options['en_sha384']).grid(row = 3, column = 0)
        Entry(encodings, textvariable = self.options['SHA384'], width = 45).grid(row = 3, column = 1, columnspan = 2)

        #Label(encodings, text = 'SHA512:').grid(row = 4, column = 0)
        Checkbutton(encodings, text="SHA512", variable=self.options['en_sha512']).grid(row = 4, column = 0)
        Entry(encodings, textvariable = self.options['SHA512'], width = 45).grid(row = 4, column = 1, columnspan = 2)

        # Buttom Buttons frame
        buttons = LabelFrame(self, text = 'Options', relief = GROOVE, labelanchor = 'nw', width = 440, height = 100)
        buttons.grid(row = 2, column = 1)
        buttons.grid_propagate(0)

        # Bottom buttons
        show_hashes = Button(buttons, text = "HASH", command = self.hash_all, width = 53).grid(row = 0, column = 0, columnspan = 3)
        exit_app = Button(buttons, text = "EXIT", command = exit, width = 53).grid(row = 1, column = 0, columnspan = 3)

    def file_browser(self):
        self.options['file'].set(askopenfilename())

    def hash_all(self):

        if self.options['en_md5'].get() == 1:
            self.options['MD5'].set(self.md5())

        if self.options['en_sha1'].get() == 1:
            self.options['SHA1'].set(self.sha1())

        if self.options['en_sha256'].get() == 1:
            self.options['SHA256'].set(self.sha256())

        if self.options['en_sha384'].get() == 1:
            self.options['SHA384'].set(self.sha384())

        if self.options['en_sha512'].get() == 1:
            self.options['SHA512'].set(self.sha512())

        hashes = {'md5': self.options['MD5'].get(),
            'sha1': self.options['SHA1'].get(),
            'sha256': self.options['SHA256'].get(),
            'sha384': self.options['SHA384'].get(),
            'sha512': self.options['SHA512'].get(),
            }

        # Search a match with given hash
        if self.options['hash'].get():
            for encoding, hash in hashes.items():
                if hash == self.options['hash'].get():
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

    def exit(self, event):
        # This is a work around to avoid a debug message that shows a key was pressed and executed the close command.
        self.destroy()

main = MainWindow()
main.mainloop()
