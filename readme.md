This is the Django portion of the example.

This represents a server-side rendered application that one wants to transtion to an API driven application.


**Run locally**

This this example applicaiton locally by navigating to the `s3test` directory and starting the builtin server.
Start the server with `./manage.py runserver 127.0.0.1:8000`.

**Use local ember application**

To use a local ember application, change the url in the `s3test/trythis/templatetags/s3.py` file to `localhost:4200`.

Depending on the name of the ember applicaiton, the `reversed(resources)` function may need to be removed so that the `vendor` files are output first.
