Katie DJ -- Data broadcast
=============================

## **Note** The websocket server at ws://katiedj.com is not active anymore. Contact me if you want a backup of the database.

[http://katiedj.com](http://katiedj.com)

This repository contains the source code for [http://katiedj.com](http://katiedj.com), released under the MIT license. You should have received a copy of the license along with the code. If not, then please visit the official license page [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).


## Background

Katie DJ is the first free traffic data broadcast. In other words, is a web platform that streams data related to road network traffic (e.g., number of vehicles in the streets). Such data are open and accessible to everyone.

  - No registration is required.
  - No email is asked.
  - No information at all is asked: data is simply broadcast to the world and anyone can "listen to" (read, download) it.


## What, Why, How?

Please refer to the Frequently Asked Questions at [http://www.katiedj.com/#faq](http://katiedj.com/#faq). Furthermore, if some question of yours is not answered there then we encourage to get in touch with us. The easiest way to do so is to open a ticket/issue in this repository.


## Download data

Data are accessible to everyone, without any limitation. Differently said, you can write your own piece of code that listen to the broadcast and you can use the data as you like. However, to ease this task, we decided to release software client too, so that you can use them instead of spending time in writing your own.

These software clients are also entirely free and open-source, and they are published [here](https://github.com/pgrandinetti/katiedj-listeners).


## Agenda

This is an experimental platform built for scientists. We plan on releasing as many software listener as we can (for the most common programming languages) and also on integrating microscopic traffic simulator such as [SUMO](http://sumo.dlr.de/index.html)


## Comments, Bug reports and Feature requests

We will really appreciate any comment or bug report that comes in, and we are totally open to feature requests, as this is an experimental platform thought for scientists. Please, feel free to open a ticket [here](https://github.com/pgrandinetti/katiedj/issues) to get in touch with any type of comment. Thank you!


## Contributing

External contribution is definitely welcome, in any form. Please do no hesitate to send to us your opinion about Katie DJ, your ideas about some additional feature. Furthermore, you can fork this repository to work on different ideas, or you can submit a merge request if you think we should integrate something of yours.


## Credits

Katie DJ development is based on Python and relies on the following libraries:

  - Django
  - Channels (with Daphne, Asigref)
  - Websockets
  - pytest


## Developer's guide

If you want to fork (or clone) KatieDJ's web server, and reproduce it, here are the steps that you should follow:

  1. Clone the repository. For example (in some Linux distributions): `git clone https://github.com/pgrandinetti/katiedj.git ~/katiedj`
  2. Create and activate a new python virtual environment. The current development was done under Python 3.5.2, but more recent versions should also work.
  3. Move into the project folder. For example: `cd ~/katiedj`.
  4. Install all required packages into the new virtualenv: `pip install -r requirements.txt`.
  5. Create the file `main/settings/secret.py`. See below for details.
  6. You are now ready to go. For example, in your local environment you can do `python manage.py runserver --settings=main.settings.dev` and the server will start.


The `main/settings/secret.py` is where we store secret information such as passwords and API keys, and it's not versioned with git. You will have to create it and add into it the information required for a realistic deployment. For example, in katiedj.com server the `secret.py` looks like the following:

```
from os import environ
import json

environ["SECRET_KEY"] = "django-secret-key--required"
environ["EMAIL_HOST_USER"] = "something--not required at the moment"
environ["EMAIL_HOST_PASSWORD"] = "some-passw--not required at the moment"
environ["EMAIL_USE_TLS"] = "True"
environ["EMAIL_PORT"] = "some-digits--not required at the moment"
environ["EMAIL_HOST"] = "some-host--not required at the moment"

# API KEYS for publishers
#
# (key, value) pairs of (string, list[string])
# When a request arrives with a valid *key*,
# the message can be broadcasted only to channels whose name is contained in the corresponding *value*.
# If the request doesn't contain any valid key then it's answered with a error.
# See publisher/views.py:PublisherView
keys = {
    # "sample_net" the channel name defined in main/consumers.py:SampleNetwork
    'some-long-secret-string': ['sample_net'],
}
environ["API_KEYS"] = json.dumps(keys)
```

### Unit tests

Just run `pytest --ds=main.settings.dev` to see the tests executed.
