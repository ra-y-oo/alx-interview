# 0x01.Lockboxes

## Description

Contains a python function:

```python
def canUnlockAll(boxes)
```

```boxes``` is  a list of lists. The function determines if a list boxes can be opened.

## Problem Definition

You have ```n``` number of locked boxes in fron tof you. Each box is numbered sequentially from ```0``` to ```n-1``` and each box may contain keys to the other boxes. Define a method that determines if the boxes can be opened. Return ```True``` if all boxes can be opened, else return ```False```

## How to run

Call the function at the bottom of the python file and add thr list of boxes:

```python
boxes = [[1],[2],[3],[4]]
print(canUnlockAll(boxes)) # Output: True
```
