
---

# What is Multithreading in Python?

-> **Multithreading** = running multiple threads (tasks) **concurrently within a single process**

-> Threads share:

* same memory space
* same variables

---

#  Simple Definition

> Multithreading allows a program to execute multiple tasks concurrently using lightweight threads within the same process.

---

#  Why Use Multithreading?

✅ Best for:

* API calls
* File I/O
* Database queries
* Network requests

❌ Not ideal for:

* CPU-heavy tasks (due to GIL)

---

# GIL (Very Important)

-> **GIL = Global Interpreter Lock**

* Only **one thread executes Python bytecode at a time**
* Limits CPU parallelism

-> So:

* Multithreading = concurrency (not true parallelism)

---

#  Basic Syntax

```python
import threading

def task():
    print("Running task")

t = threading.Thread(target=task)
t.start()
t.join()
```

---

#  Explanation

* `target` → function to run
* `start()` → starts thread
* `join()` → waits for completion

---

#  Example 1: Without Multithreading

```python
import time

def task(n):
    time.sleep(2)
    print(f"Task {n} done")

for i in range(3):
    task(i)
```

-> Total time ≈ **6 sec**

---

#  Example 2: With Multithreading

```python
import threading
import time

def task(n):
    time.sleep(2)
    print(f"Task {n} done")

threads = []

for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

-> Total time ≈ **2 sec**

---

#  Thread with Arguments

```python
t = threading.Thread(target=task, args=(1,))
```

-> `args` must be tuple

---

# Thread Synchronization (Lock)

-> Avoid race conditions

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
```

---

#  Without Lock → Wrong Output

-> Multiple threads modify shared variable incorrectly

---

#  ThreadPoolExecutor (Best Practice)

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n*n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(task, [1,2,3,4]))

print(results)
```

---

#  Real Data Engineering Example

### Parallel API Calls

```python
import requests
from concurrent.futures import ThreadPoolExecutor

urls = ["url1", "url2", "url3"]

def fetch(url):
    return requests.get(url).status_code

with ThreadPoolExecutor(max_workers=3) as ex:
    results = list(ex.map(fetch, urls))
```

---

# Multithreading vs Multiprocessing

| Feature | Multithreading | Multiprocessing |
| ------- | -------------- | --------------- |
| Memory  | Shared         | Separate        |
| Speed   | I/O fast       | CPU fast        |
| GIL     | Affected       | Not affected    |

---

#  When to Use What

* I/O tasks → **Multithreading**
* CPU tasks → **Multiprocessing**

---

#  Interview Explanation (Perfect)

> “Multithreading in Python is used for concurrent execution of I/O-bound tasks. Due to the GIL, it doesn’t provide true parallelism for CPU-bound tasks, so multiprocessing is preferred there.”

---

#  Common Interview Questions

* What is GIL?
* Thread vs Process?
* Race condition?
* When to use ThreadPoolExecutor?

---

#  Pro Tips

* Always use `ThreadPoolExecutor` in production
* Use locks when sharing data
* Avoid too many threads

---

#  Final Takeaway

* Multithreading = concurrency
* Best for I/O tasks
* GIL limits CPU usage
* Use thread pools for scalability

---

