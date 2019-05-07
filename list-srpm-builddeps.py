#!/usr/bin/env python3

import rpm
import sys
from optparse import OptionParser

def valid_cpu_type(s):
    return s == "x86_64" or s == "aarch64"

def parse_arguments():

    parser = OptionParser()

    parser.add_option("-t", "--target-cpu", dest="cpu",
                      help="target cpu name",
                      metavar="target_cpu", default="x86_64")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        print("must be specify .spec file path", file=sys.stderr)
        exit(-1)

    if not valid_cpu_type(options.cpu):
        print("valid cpu type is x86_64, aarch64", file=sys.stderr)
        exit(-1)

    return {
        "cpu": options.cpu,
        "spec": args[0],
    }

if __name__ == "__main__":

    args = parse_arguments()
    specfile = args["spec"]
    
    rpm.addMacro("_target_cpu", args["cpu"])
    try:
        spec = rpm.spec(specfile)
        for dep in rpm.ds(spec.sourceHeader, "requires"):
            name = dep.DNEVR()[2:]
            print(name)
            
    except ValueError as e:
        print("error: %s" % e)
