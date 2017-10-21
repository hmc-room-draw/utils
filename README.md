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
        0.88526,
        0.24316
      ],
      [
        0.79211,
        0.24298
      ],
      [
        0.75912,
        0.20754
      ],
      [
        0.7593,
        0.11211
      ],
      [
        0.81947,
        0.11211
      ],
      [
        0.88544,
        0.17842
      ]
    ],
    "bounding_box": [
      0.75912,
      0.11211,
      0.88561,
      0.24333
    ]
  },
  "room_1": {
    "contour": [
      [
        0.88544,
        0.30877
      ],
      [
        0.79228,
        0.30895
      ],
      [
        0.79211,
        0.24632
      ],
      [
        0.88526,
        0.24614
      ]
    ],
    "bounding_box": [
      0.79211,
      0.24614,
      0.88561,
      0.30912
    ]
  }
}
```
