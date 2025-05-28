# db25-hw7-logstore

A simple append-only key-value store implemented for the Spring 2025 Databases course (DB25).  
It logs all changes to a file (`data.log`) and reconstructs its state on startup by replaying that log.

> **HW7** — Bonus multiplier: **2**

---

## 📌 Features

- `SET <key> <value>`: Stores or overwrites a key with a value
- `GET <key>`: Retrieves the value of a key (or `null` if missing)
- `DELETE <key>`: Removes a key from the store
- `DUMP`: Prints all current key-value pairs
- `EXIT`: Exits the program
- Persistent state stored in `data.log` using an append-only format
- State is reconstructed on every startup by replaying the log

---

## 📁 Project Structure

```
db25-hw7-logstore/
├── logstore/
│   ├── __init__.py
│   └── store.py          # Core KeyValueStore class
├── tests/
│   ├── __init__.py
│   └── test_store.py     # Pytest test suite for store.py
├── main.py               # CLI entry point
├── data.log              # Auto-generated log file
├── .gitignore
└── README.md
```

---

## 🔧 How to Run

```bash
git clone https://github.com/Alain-David-001/db25-hw7-logstore.git
cd db25-hw7-logstore
python main.py
```

---

## ▶️ Example CLI Usage

```text
🔑 Welcome to the Append-Only Key-Value Store
Type SET <key> <value>, GET <key>, DELETE <key>, DUMP, or EXIT
> SET name Alain
> SET language Python
> GET name
Alain
> DELETE name
> GET name
(null)
> DUMP
language: Python
> EXIT
```

After restarting the program, the state is restored automatically from `data.log`.

---

## 🧪 Testing

Run the test suite using:

```bash
pytest
```

Covers:
- Setting, getting, and deleting keys
- Overwriting existing values
- Rebuilding state from a sample log

---

## 🧠 Notes

- The log file grows over time; there is no compaction or pruning.
- Each operation is logged immediately — crash-safe but not optimized for space.
- Keys and values are stored as strings.

---

## 🧑‍💻 Author

**Alain David Escarrá García**  
2nd-year Software, Data, and Technology student  
Constructor University, Spring 2025
