import sys
import os
import time

from syscleaner.commands import (
    update_system,
    clean_system,
    show_info,
    repair_system
)

def menu():
    
    if len(sys.argv) < 2:
        print("Usage: syscleaner <command>")
        print("Commands:")
        print("  update   - Update and upgrade the system")
        print("  clean    - Clean up unnecessary packages")
        print("  info     - Show system information")
        print("  repair   - Repair broken packages")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "update":
        update_system()
    elif command == "clean":
        clean_system()
    elif command == "info":
        show_info()
    elif command == "repair":
        repair_system()
    else:
        print("Unknown command. Use 'update', 'clean', 'info', or 'repair'.")
        sys.exit(1)

def main():
    menu()


if __name__ == "__main__":
    main()