# utils

## `roomfinder.py` instructions

Export each PDF Andrew gave us as a tiff image with 300 px/in resolution.
Install OpenCV via `pip3 install openvc-python`, then run `python3
roomfinder.py -i <IMAGE>`. Click on rooms to select them, then hit `q` to quit.
JSON specifying the rooms' geometry (in relative coords, not pixels) will be
printed to `stdout`.

```
{
  "room_0": [
    [
      0.39294,
      0.34
    ],
    [
      0.27216,
      0.34121
    ],
    [
      0.2698,
      0.29818
    ],
    [
      0.39059,
      0.29697
    ]
  ],
  "room_1": [
    [
      0.35922,
      0.29394
    ],
    [
      0.27059,
      0.29455
    ],
    [
      0.2698,
      0.25091
    ],
    [
      0.35843,
      0.2503
    ]
  ], ...
}
```
