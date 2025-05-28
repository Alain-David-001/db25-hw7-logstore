import os
import pytest
from logstore.store import KeyValueStore

TEST_LOG_FILE = "test_data.log"

@pytest.fixture
def clean_store():
    # Ensure the test log file is removed before each test
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)
    yield KeyValueStore(log_file=TEST_LOG_FILE)
    # Clean up after test
    if os.path.exists(TEST_LOG_FILE):
        os.remove(TEST_LOG_FILE)

def test_set_and_get(clean_store):
    clean_store.set("name", "Alain")
    assert clean_store.get("name") == "Alain"

def test_overwrite_value(clean_store):
    clean_store.set("language", "Python")
    clean_store.set("language", "Rust")
    assert clean_store.get("language") == "Rust"

def test_delete_existing_key(clean_store):
    clean_store.set("framework", "FastAPI")
    clean_store.delete("framework")
    assert clean_store.get("framework") is None

def test_delete_nonexistent_key(clean_store):
    # Should not raise error
    clean_store.delete("nonexistent")
    assert clean_store.get("nonexistent") is None

def test_log_replay():
    # Write log manually
    with open(TEST_LOG_FILE, 'w') as f:
        f.write("SET name Alain\n")
        f.write("SET lang Python\n")
        f.write("DELETE name\n")
        f.write("SET lang Rust\n")

    kv = KeyValueStore(log_file=TEST_LOG_FILE)
    assert kv.get("name") is None
    assert kv.get("lang") == "Rust"
