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
    "contour": [
      [
        0.36364,
        0.16235
      ],
      [
        0.33091,
        0.16157
      ],
      [
        0.33182,
        0.05255
      ],
      [
        0.3803,
        0.05333
      ],
      [
        0.3803,
        0.14353
      ]
    ],
    "bounding_box": [
      0.33091,
      0.05255,
      0.0497,
      0.1102
    ]
  },
  "room_1": {
    "contour": [
      [
        0.43121,
        0.16196
      ],
      [
        0.38182,
        0.16157
      ],
      [
        0.38212,
        0.05294
      ],
      [
        0.43152,
        0.05333
      ]
    ],
    "bounding_box": [
      0.38182,
      0.05294,
      0.05,
      0.10941
    ]
  }
}
```
