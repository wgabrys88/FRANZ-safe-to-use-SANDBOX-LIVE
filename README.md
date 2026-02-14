# Yep, it works, look at this:
---------------------------
I learned that the `left_click` function call was malformed because it lacked parentheses. The correct syntax is `left_click(x, y)`.

My plan:
1. Correct the function calls by adding proper parentheses.
2. Then proceed with a drag from (370, 60) toward lower-left corner as described earlier.

I will now execute the corrected command:

```python
left_click(370, 60)
drag(370, 60, 150, 800)
```

After executing these steps, I'll check if they worked properly.

------------------------------
Download all the files, run python main.py and thats it (windows 11 only and python 3.13 only, LM Studio (everything just grab and download in latest version)
The panel Script is just a "wireshark" that allows to watch the api communication between the python and lm studio, tun it or not, run if you want to see something.

By default this repo is set to Sandbox mode (it uses blank image file on disc and the pipeline/system thinks that it is real dekstop, and it adapts, thinks its a paint app, and so on)

This when run will train a persona (System Prompt) of any agent you want - Visual one of course, we dont use here any "skills" or apis to connect to software,
we are Entity - it sees and moves mouse and keyboard the same way as humans, this is different level my brothers! Have a Good Weekend!
