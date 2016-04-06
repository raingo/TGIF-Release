#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

from string import Template

g = '''
<div class="gold">
    <img src="$url" alt="" height="128" />
    <p>$text</p>
</div>
'''

def main():
    import sys

    output = []
    gold = Template(g)

    for line in sys.stdin:
        fields = line.strip().split('\t')
        output.append(gold.substitute(url = fields[0], text = fields[1]))

    print '\n'.join(output)

    pass

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
