import time
outputs = []


def canary():
    # NOTE: you must add a real channel ID for this to work
    outputs.append(
        ["C07HXBJ79",
         "Gilhooly bot exiting hibernation. Please move away from the door: " +
         str(time.time())])


canary()
