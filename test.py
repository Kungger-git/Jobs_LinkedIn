import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='+')
print('--foo 1 2 3'.split())
args = parser.parse_args('--foo 1 2 3'.split())
print(args)
print(args.foo)
