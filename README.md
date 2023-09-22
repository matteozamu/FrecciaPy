# FrecciaPy

I got bored while on a train journey so I decided to have some fun.

FrecciaPy is a simple client to display information about your [Frecciarossa](https://www.trenitalia.com/en/frecce/frecciarossa.html) train in your terminal.

The "PortaleFrecce WiFi" (https://www.portalefrecce.it) onboard the train has an endpoint which expose: `speed`, `delay`, `progress of the journey`, `next stops` and `connections`.

The client does a simple HTTP GET request to the endpoint and display the information nicely in the terminal.

Just run the python code with:

```
python3 main.py
```

![Screenshot](https://raw.githubusercontent.com/matteozamu/FrecciaPy/main/example.png)

I was inspired by [TerminalGV](https://github.com/TheStaticTurtle/TerminalGV) which works on TGV and TER trains in France.
