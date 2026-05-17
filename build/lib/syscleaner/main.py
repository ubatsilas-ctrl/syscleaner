import sys

from syscleaner.commands import (
    update_system,
    clean_system,
    show_info,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: syscleaner [update|clean|info]")
        return

    command = sys.argv[1].lower()

    if command == "update":
        update_system()
    elif command == "clean":
        clean_system()
    elif command == "info":
        show_info()
    else:
        print("Unknown command. Use 'update', 'clean', or 'info'.")

if __name__ == "__main__":    main()