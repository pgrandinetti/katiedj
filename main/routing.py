from main import consumers
from channels import include as ch_include

macro_routing = [
    consumers.SampleNetwork.as_route(path=r"^/sample/"),
]

channel_routing = [
    ch_include(macro_routing, path=r"^/macro"),
]
