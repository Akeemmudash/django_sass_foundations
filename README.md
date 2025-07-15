# Django SaaS Starter

This project is a SaaS (Software-as-a-Service) application built with **Python & Django**. It includes recurring payments via Stripe, a modern UI using TailwindCSS & Flowbite, PostgreSQL with Neon, CI/CD pipelines with GitHub Actions, and more.

## 🚀 Features

- Django 5 project structure
- User authentication via Django AllAuth (email + GitHub login)
- Stripe integration for recurring payments (Products/Prices API)
- Neon serverless PostgreSQL database
- GitHub Actions for CI/CD & scheduled tasks
- Deployable to Railway using Docker
- TailwindCSS + Flowbite styling
- Custom Django management commands
- Role-based access control (Groups & Permissions)
- Email setup with Gmail
- Whitenoise for static file serving

## 🔧 Tech Stack

- Python / Django
- Stripe
- Neon PostgreSQL
- TailwindCSS / Flowbite
- GitHub Actions
- Railway
- Docker
- Python Decouple

## 🛠️ Setup

```bash
git clone https://github.com/akeemmudash/django_saas_foundations.git
cd django_saas_foundations
pip install -r requirements.txt
python manage.py runserver
