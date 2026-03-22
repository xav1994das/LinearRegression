import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", help="marks for physics")
    parser.add_argument("--chemistry", help="marks for chemistry")
    parser.add_argument("--maths", help="marks for math")
    args=parser.parse_args()

    res=(float(args.physics)+float(args.chemistry)+float(args.maths))/3
    print(res)