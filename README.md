# 🧬 pop-forge

**pop-forge** is a personal automation toolkit for setting up my development workspace quickly and consistently. It centralizes all my automation scripts into a single entry point and handles everything from cloning repositories, installing essential tools, downloading apps, and preparing the environment I work in — all with minimal manual effort.

---

## 🧠 Motivation

Setting up a new machine or refreshing a development environment often means repeating the same steps:

* Cloning private and public automation scripts
* Installing the software I use daily
* Running custom post-install configurations

**pop-forge** is my way of automating all of this in one script.

---

## 📦 Features

* ✅ Clone personal automation repositories
* ✅ Download and install required software
* ✅ Centralized entry point for all provisioning scripts
* ✅ Easy to update and extend

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/davieduardo001/pop-forge.git
cd pop-forge
```

### 2. Run the main script

> ⚠️ **Make sure you trust the script and understand what it does before running.**

```bash
chmod +x script.py
python script.py
```

This will:

* Clone my core automation script repositories
* Trigger the setup process using helper scripts inside the `scripts/` folder

---

## 🗃️ Project Structure

```
pop-forge/
├── script.py         # Main script that orchestrates the setup
├── scripts/          # Folder for modular automation scripts
└── .gitignore
```

---

## 🧰 Requirements

Currently designed to work on:

* Linux-based systems (Pop!\_OS, Ubuntu, etc.)

Python 3 must be installed.

---

## 🔧 Customization

This project is made for personal use but feel free to fork it and tweak the scripts for your own setup.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🧑‍💻 Author

Made with 💻 by [davieduardo001](https://github.com/davieduardo001) — to simplify my own life and maybe yours too.
