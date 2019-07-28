import json
import requests
from car.Part import Part


class Client(Part):

    def __init__(self, name, input_names, is_localhost, port=8092, url='/command', is_verbose=False):
        super().__init__(
            name=name,
            is_localhost=is_localhost,
            port=port,
            url=url,
            input_names=input_names,
            is_verbose=is_verbose
        )

    # The parent class, Part.py, automatically runs this function an in infinite loop
    def request(self):
        response = requests.post(
            self.endpoint,
            data=json.dumps(self.inputs)
        )

    # This is how the main control loop interacts with the part
    def call(self, *args):
        self.inputs = dict(zip(self.input_names, *args))

    def brake(self):
        response = requests.post(
            self.endpoint,
            data=json.dumps(self.inputs)
        )
