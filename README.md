# Hospital Management System

Modern, role-based hospital management application for scheduling appointments, managing patient records, coordinating doctors and receptionists, and sending automated email notifications. Built to be easy to run locally and straightforward to extend.

## Overview

The system models three primary roles:
- Admin: manages doctors, patients, and receptionists with full CRUD access.
- Doctor: views assigned appointments and patient info for upcoming consultations.
- Receptionist: books appointments, registers patients, and updates patient details.

Core workflows:
- Registration for Doctors and Patients with validation.
- Appointment booking with doctor selection, date, and time.
- Email notifications for new registrations and booked appointments.
- Admin dashboards for user management and oversight.

## Features

- Role-based access (Admin, Doctor, Receptionist/Patient)
- Patient onboarding and profile management
- Doctor directory and assignment
- Appointment booking, listing, and status tracking
- Email notifications for registrations and appointments
- MySQL-backed persistent storage
- Modular design for future expansion (billing, prescriptions, inventory)

## Tech Stack

- Backend: Java
- UI: Java Swing
- Database: MySQL
- Email: SMTP (configurable sender)

Note: If your implementation uses a different stack (e.g., Python/Django, Node/Express, etc.), adjust the Setup and Configuration sections accordingly.

## Getting Started

### Prerequisites
- Java 8+ and a Java IDE (IntelliJ IDEA/NetBeans/Eclipse)
- MySQL 5.7+ (or MariaDB)
- SMTP credentials for email sending

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adityakryadav/project_hospital-management.git
   cd project_hospital-management
   ```
2. Create the database and tables using the provided SQL file:
   ```sql
   -- If your repo includes hospital.sql:
   -- Execute it in MySQL (CLI or phpMyAdmin/MySQL Workbench)
   SOURCE path/to/hospital.sql;
   ```
3. Configure database credentials:
   - Locate the Connector/DB configuration class in the source (e.g., `Connector`).
   - Set `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASSWORD` to match your local MySQL instance.
4. Configure email sending:
   - Locate the email utility class (e.g., `EmailSystem`).
   - Set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, and `SENDER_EMAIL`.
5. Build and run:
   - From your IDE, run the main application class.
   - Or use your build tool (e.g., Ant/Maven/Gradle) if present in the project.

## Configuration

Environment-style settings (adjust based on your implementation):
- Database:
  - DB_HOST=localhost
  - DB_PORT=3306
  - DB_NAME=hospital
  - DB_USER=root
  - DB_PASSWORD=your_password
- Email:
  - SMTP_HOST=smtp.yourprovider.com
  - SMTP_PORT=587
  - SMTP_USER=your_email@domain.com
  - SMTP_PASSWORD=app_specific_password
  - SENDER_EMAIL=your_email@domain.com

Store credentials securely (e.g., environment variables, local config files excluded from VCS). Do not hardcode secrets.

## Database Schema

The typical schema includes:
- Admin: username, password
- Doctor: profile and login details
- Patient: profile details
- Receptionist: profile and login details
- Appointment: links doctor and patient with date/time and notes

Refer to `hospital.sql` if present for exact definitions and keys.

## Usage

- Admin
  - Register doctors and receptionists
  - View and manage patients, appointments, and staff
- Doctor
  - View assigned appointments and patient details
  - Review schedule
- Receptionist
  - Register patients
  - Book and update appointments

## Email Notifications

- On successful registration of Doctor/Patient, a confirmation email is sent.
- When an appointment is booked:
  - Patient receives appointment details.
  - Assigned Doctor receives their upcoming schedule.

Ensure SMTP credentials are valid and network access to the SMTP server is permitted.

## Project Structure

Common layout (your structure may vary):
```
project_hospital-management/
├─ src/                    # Application source (packages, UI, services, models)
├─ hospital.sql            # Database schema and seed data
├─ build.xml / pom.xml     # Build configuration (Ant/Maven) if applicable
├─ dist/                   # Build artifacts
├─ README.md               # This file
```

## Roadmap

- Add user password hashing and secure credential storage
- Appointment approval flow for Doctors
- Role-based authorization hardening
- Billing, invoices, and payment tracking
- Audit logs and activity tracking
- REST API endpoints for web/mobile clients

## Contributing

Contributions are welcome:
- Fork the repo and create a feature branch
- Follow existing code style and patterns
- Add tests where applicable
- Open a pull request with a clear description

## License

Lisence @ FOT, University of Delhi

## Acknowledgements

- Common hospital management workflows and schema patterns
- Community references for appointment and notification flows

