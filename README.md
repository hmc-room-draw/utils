# utils

## `roomfinder.py` instructions

Export each PDF Andrew gave us as a tiff image with 300 px/in resolution.
Install OpenCV via `pip3 install openvc-python`, then run `python3
roomfinder.py -i <IMAGE>`. Click on rooms to select them, then hit `q` to quit.
JSON specifying the rooms' geometry (in relative coords, not pixels) will be
printed to `stdout`.

`contour` is given as a list of points. `bounding_box` is given as a list of
values `x,y,w,h`; you can make a `div` element out of the latter quite easily.

```
{
  "room_0": {
    "bounding_box": {
      "x": 0.38182,
      "y": 0.05294,
      "w": 0.05,
      "h": 0.10941
    }
  },
  "room_1": {
    "bounding_box": {
      "x": 0.33091,
      "y": 0.05255,
      "w": 0.0497,
      "h": 0.1102
    }
  }
}
```
