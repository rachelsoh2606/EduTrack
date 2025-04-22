# Programming-Principle Final Assignment
# EduTrack 🎓  
**Student Assignment, Attendance, and Timetable Management System**

## 📖 Project Description
**EduTrack** is a command-line academic portal built in Python for students and lecturers. It combines essential academic management features like assignment submission, attendance check-in via secure codes, and timetable organization—all in one terminal-based interface.

The system ensures improved academic tracking, student accountability, and a simplified process for lecturers to manage classroom logistics.

---

## 🚀 Key Features

### ✅ Assignment Management
- Submit assignments with PDF upload prompt
- Faculty can update course code, assignment name, status, and student ID
- Display all assignment data in a formatted table

### 📅 Timetable Management
- Create, update, delete, and view weekly timetables
- Prevents overlapping time slots and enforces proper scheduling rules

### 🕐 Attendance System
- Lecturers generate secure 5-digit codes for lecture check-ins
- Codes expire after 15 minutes to ensure real-time check-in
- Students check in using the code, and attendance percentages are auto-calculated

### 👥 Role-Based Menu System
- **Lecturer Mode**: Generate check-in codes, monitor attendance
- **Student Mode**: Submit assignments, mark attendance, manage timetable

---

## 🛠 Technologies Used
- **Python 3.x**
- **Tkinter** (for file dialog)
- **Built-in libraries**: `os`, `datetime`, `random`
- **Text File Storage**:
  - `assignments_StudentID.txt`
  - `attendance_StudentID.txt`
  - `timetables_StudentID.txt`

---

## 💻 Setup / Installation Instructions

### 1. Requirements
- Python 3.x installed
- Works best on **Windows OS** (due to `os.system('cls')`)

### 2. Install Required Modules (if not pre-installed)
```bash
pip install tk
