# ⚡ Parallel and Distributed Computing

> **CS32** — 3rd Year, 2nd Semester  
> A hands-on exploration of concurrency, parallelism, and distributed computing concepts using Python.

---

<p align="center">
  <strong>🖥️ Threads · Processes · Executors · Futures</strong>
</p>

---

## 👥 Team

<div align="center">

<table>
<tr>
<td align="center" width="50%" valign="top">
  <img src="https://github.com/hdmGOAT.png" width="88" height="88" alt="Hans Matthew Del Mundo" /><br />
  <strong>Hans Matthew Del Mundo</strong><br />
  <a href="https://github.com/hdmGOAT"><kbd>@hdmGOAT</kbd></a>
</td>
<td align="center" width="50%" valign="top">
  <img src="https://github.com/potakaaa.png" width="88" height="88" alt="Gerald Helbiro Jr." /><br />
  <strong>Gerald Helbiro Jr.</strong><br />
  <a href="https://github.com/potakaaa"><kbd>@potakaaa</kbd></a>
</td>
</tr>
<tr>
<td align="center" width="50%" valign="top">
  <img src="https://github.com/areeesss.png" width="88" height="88" alt="Vin Marcus Gerebise" /><br />
  <strong>Vin Marcus Gerebise</strong><br />
  <a href="https://github.com/areeesss"><kbd>@areeesss</kbd></a>
</td>
<td align="center" width="50%" valign="top">
  <img src="https://github.com/unripelo.png" width="88" height="88" alt="Ira Chloie Narisma" /><br />
  <strong>Ira Chloie Narisma</strong><br />
  <a href="https://github.com/unripelo"><kbd>@unripelo</kbd></a>
</td>
</tr>
</table>

</div>

---

## 📖 About

This repository contains laboratory exercises and projects for **Parallel and Distributed Computing (PDC)**. Each lab builds on core concepts—from basic concurrency primitives to task and data parallelism—using Python's standard library.

### What You'll Explore

| Concept | Description |
| :--- | :--- |
| **Concurrency** | Multiple tasks making progress over time |
| **Parallelism** | Multiple tasks executing simultaneously |
| **GIL** | Global Interpreter Lock and its implications |
| **Threading** | Lightweight execution for I/O-bound work |
| **Multiprocessing** | True parallelism for CPU-bound work |
| **Executors** | High-level abstractions for parallel execution |

---

## 🗂️ Repository Structure

```
PDC Repo/
├── lab_1/          # Python Calculator — foundational I/O and control flow
├── lab_2/          # Multithreading vs Multiprocessing — GWA calculator
├── lab_3/          # Task & Data Parallelism — Philippine payroll deductions
└── README.md
```

---

## 🧪 Labs Overview

### Lab 1 — Python Calculator
A simple interactive calculator demonstrating basic Python operations: addition, subtraction, multiplication, and division. Serves as the foundation for understanding program flow and I/O handling.

```bash
cd lab_1 && python lab1.py
```

---

### Lab 2 — Multithreading vs Multiprocessing
A **Grade Weighted Average (GWA)** calculator that compares two concurrency approaches:

- **Multithreading** — shared memory, GIL-limited, ideal for I/O-bound tasks
- **Multiprocessing** — separate processes, bypasses GIL, true parallelism for CPU-bound work

Explores data chunking, locks, queues, and the trade-offs between thread and process overhead.

```bash
cd lab_2 && python lab2.py
```

---

### Lab 3 — Task and Data Parallelism
A **Philippine payroll deduction calculator** using `concurrent.futures.ThreadPoolExecutor`:

- Computes **SSS**, **PhilHealth**, **Pag-IBIG**, and **income tax** (TRAIN law)
- Demonstrates **task parallelism** (different deduction types in parallel)
- Uses `submit()` and `Future` objects for concurrent execution

```bash
cd lab_3 && python lab3.py
```

---

## 🛠️ Requirements

- **Python 3.8+**
- No external dependencies — uses only the standard library (`threading`, `multiprocessing`, `concurrent.futures`)

---

## 📚 Key Takeaways

- **GIL** limits true parallelism in threads; use **multiprocessing** for CPU-bound work
- **Threading** excels at I/O-bound tasks with minimal overhead
- **ProcessPoolExecutor** enables true parallelism; **ThreadPoolExecutor** is lighter for I/O
- **Task parallelism** = different tasks; **Data parallelism** = same task on different data

---

<p align="center">
  <em>Built for CS32 — Parallel and Distributed Computing</em>
</p>
