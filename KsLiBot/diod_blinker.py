import RPIO
import time

OUT_24 = 24

def main():

	# set up output channel with an initial state
    RPIO.setup(OUT_24, RPIO.OUT, initial=RPIO.LOW)

    for i in range(10):
        RPIO.output(OUT_24, 1)
        time.sleep(1)
        RPIO.output(OUT_24, 0)
        time.sleep(1)

    # reset every channel that has been set up by this program,
    # and unexport interrupt gpio interfaces
    RPIO.cleanup()

if __name__ == '__main__':
    main()