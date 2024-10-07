# this code is for print zzig zag pattern unless user stop.
import time,sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end='')
        print("****")
        time.sleep(0.1)

        # change direction in zig zag form.
        if indentIncreasing:
            indent += 1
            if indent == 5:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    print('\n Exiting Time...')
    sys.exit()