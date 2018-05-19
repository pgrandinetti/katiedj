Katie DJ -- Data broadcast
=============================

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
