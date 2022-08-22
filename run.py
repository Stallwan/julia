import argparse
import numpy as np
import matplotlib.pyplot as plt

from src.julia import Julia


if __name__ == "__main__":
    
    julia = argparse.ArgumentParser(prog="jfg", description="Julia fractal generator.") 

    julia.add_argument("pixeldensity", type=int, help="quality. Would be around 1000")
    julia.add_argument("detaildensity", type=int, help="finesse. Would be around 100")
    julia.add_argument("c", type=float, nargs=2, help="complex number 'c' being the starting point of the fractal")

    julia.add_argument("-c", "--colors", type=str, help="to choose the color")

    args = julia.parse_args()

    
    c = complex(args.c[0], args.c[1])

    j = Julia
    plan = j.create_complex_matrix(-4, 4, -4, 4, args.pixeldensity)
    julia = j.new(plan, c, args.detaildensity)

    plt.figure(figsize=(10, 10))

    if args.colors:
        plt.imshow(julia, cmap=args.colors)
        plt.show()       

    else:
        plt.imshow(julia, cmap="hsv")
        plt.show()       

