import subprocess

import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface" , dest="interface", help="interface to change its MAC address ")


parser.parse_args()


interface = raw_input(" interface > ")

new_mac = raw_input(" new mac >")


