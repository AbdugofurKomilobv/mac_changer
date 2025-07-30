import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

if not options.interface:
    options.interface = input("Interface > ")

if not options.new_mac:
    options.new_mac = input("New MAC > ")

print(f"[+] Changing MAC address for {options.interface} to {options.new_mac}")

subprocess.call(["ifconfig", options.interface, "down"])
subprocess.call(["ifconfig", options.interface, "hw", "ether", options.new_mac])
subprocess.call(["ifconfig", options.interface, "up"])
