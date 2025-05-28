from logstore.store import KeyValueStore

def main():
    kv = KeyValueStore()
    print("🔑 Welcome to the Append-Only Key-Value Store")
    print("Type SET <key> <value>, GET <key>, DELETE <key>, DUMP, or EXIT")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not line:
            continue

        parts = line.split(maxsplit=2)
        cmd = parts[0].upper()

        if cmd == "SET" and len(parts) == 3:
            kv.set(parts[1], parts[2])
        elif cmd == "GET" and len(parts) == 2:
            value = kv.get(parts[1])
            print(value if value is not None else "(null)")
        elif cmd == "DELETE" and len(parts) == 2:
            kv.delete(parts[1])
        elif cmd == "DUMP":
            for k, v in kv.items():
                print(f"{k}: {v}")
        elif cmd == "EXIT":
            break
        else:
            print("❌ Unknown or malformed command.")

if __name__ == "__main__":
    main()
