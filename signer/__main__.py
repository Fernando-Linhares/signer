from signer.file.manager import Manager
from signer.security.signature import Signature
import re

class Signer:

    _password: str

    _file: str

    def __init__(self, props):
        self._props = props

    def execute(self):

        for prop in self._props:

            if re.search("^--password=.*", prop):
                self.arg_password(prop)

            if re.search("^--file=.*", prop):
                self.arg_file(prop)

       # signature = Signature()

        #signature.sign(self._password, self._file)



    def arg_password(self, password):

        key, value = password.split('=')

        self._password = value

    def arg_file(self, file):

        key, value = file.split('=')

        self._file = value