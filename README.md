# YourRecruiter Project 
# Smart Contract Driven Internship & Skill Matching Platform

## 📌 Project Overview

This project is an early-stage backend MVP for a **Smart Contract Driven Internship & Skill Matching Platform**.

The long-term vision is to connect students and companies using **verified skills**, **wallet-based identity**, and **blockchain-backed agreements**.  
For this current submission, the focus is intentionally placed on **backend domain modeling and architecture**, rather than full feature implementation.

--- 

## 🎯 Objective of This MVP

The goal of this version is to demonstrate:

- Clear understanding of the **business domain**
- Proper **data modeling** using Django
- Clean separation between **off-chain backend logic** and **future on-chain components**
- Ability to structure a scalable backend foundation

This MVP is **not feature-complete by design**.

---

## 🏗️ Architecture Overview

The system follows a **hybrid architecture**:

### Off-chain (Implemented)
- Django backend
- SQLite (development database)
- Django Admin for domain inspection and testing

### On-chain (Planned)
- Ethereum / Polygon blockchain
- Smart contracts (Solidity)
- Wallet-based identity (MetaMask)
- Skill verification and internship agreements on-chain

---

## 🧠 Domain Models (Implemented)

The following core domain entities are implemented and fully functional:

### 👤 CustomUser
- Single user model with role-based behavior
- Roles:
  - Student
  - Company
  - (University planned)

### 🛠️ Skill
- Represents an individual skill (e.g., Python, React, Solidity)

### 🎓 StudentSkill
- Links students to skills
- Supports verification metadata (verified / verified by)

### 💼 Internship
- Created by company users
- Contains required skills
- Includes matching criteria (minimum match percentage)

### 📄 Agreement
- Represents an internship agreement between a student and a company
- Serves as the foundation for future smart contract integration

All relationships are visible and testable via **Django Admin**.

---

## 🧪 Admin Interface

Django Admin is used as a **domain inspection tool**, allowing:

- Creation of students and companies
- Assignment and verification of skills
- Creation of internships
- Linking students to internships via agreements

This approach validates the **correctness of the data model** before building APIs or UI workflows.

---

## 🌐 Pages App (Static)

A simple `pages` app is included to provide context:

- `/` – Project overview
- `/about/` – Architecture explanation
- `/roadmap/` – Planned features and future scope

These pages are intentionally static.

---

## 🚧 Features Not Yet Implemented (Planned)

The following features are **intentionally excluded** from this MVP:

- Smart contracts (Solidity)
- Blockchain integration (Ethereum / Polygon)
- Wallet authentication (MetaMask)
- Skill verification on-chain
- Automated internship matching algorithm
- REST APIs for frontend consumption

These will be implemented in future iterations once the domain layer is stable.

---

## 🛣️ Future Roadmap

Planned next steps include:

1. Smart contract development for:
   - Skill verification
   - Internship agreements
2. Wallet-based authentication
3. REST API layer using Django REST Framework
4. Skill-based matching logic
5. React frontend integration

---

## 🧩 Why This Approach?

This project follows a **domain-first development strategy**:

> Model the problem correctly before solving it technically.

By focusing on data modeling and architecture first, future feature development becomes safer, clearer, and more scalable.

---

## ⚙️ Tech Stack (Current)

- Python 3.13
- Django
- SQLite (development)
- Django Admin

---

## 📌 Status

✅ Domain models complete  
✅ Admin interface functional  
✅ Static documentation pages added  
🚧 Advanced features planned for next phases

---

## 👨‍💻 Author Notes

This project was developed as part of a Django–Flask training program submission.  
The emphasis is on **learning, architectural thinking, and correct backend foundations**, rather than feature completeness.

---

