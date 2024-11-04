
# Project's Title

**FitFoldData:** A web tool for user-friendly analysis of circular dichroism (CD) and differential scanning calorimetry (DSC) data, integrating advanced biophysical models to enhance accessibility for researchers.

**Tool URL:** https://fit-fold-data.ung.si

# Authors

- Knarik Yeritsyan
- Artem Badasyan

# Developers

- Knarik Yeritsyan

# Project Description

This project addresses the challenges of understanding protein folding and thermal stability, which are critical in biology and pharmaceutical research. Techniques such as circular dichroism (CD) and differential scanning calorimetry (DSC) provide valuable insights, but their complex data interpretation often requires specialized knowledge, limiting accessibility for many researchers. The **FitFoldData** web tool offers a user-friendly platform for analyzing CD and DSC data, integrating the Zimm-Bragg model modified for hydrogen-bond interactions with water. Built with PHP (Laravel), JavaScript, and Python, it enables users to upload experimental data, performs real-time data fitting, calculates key parameters like glass transition temperature and hydrogen bonding energies, and provides graphical feedback—all while being open-access to democratize advanced biophysical analysis.

## Prerequisites

- **PHP 8.x** (or the version required by Laravel)
- **Composer** (for managing PHP dependencies)
- **Python 3.x** (for Python scripts)
- **pip** (Python package manager)
- **Node.js & npm** (for front-end dependencies)

## Installation

1. **Get the Project Files:**

   Download the project files and navigate to the project root directory:

   ```bash
   cd fit-fold-data
   ```

2. **Install Laravel Dependencies:**

   Run Composer to install the necessary PHP dependencies:

   ```bash
   composer install
   ```

3. **Install Python Dependencies:**

   Navigate to the directory containing your Python requirements file and install the dependencies:

   ```bash
   cd python
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**

   Copy the `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with the appropriate configurations.

5. **Generate Application Key:**

   Run this command to set the Laravel application key:

   ```bash
   php artisan key:generate
   ```

6. **Create Storage Link:**

   Run this command to link the storage directory for public access:

   ```bash
   php artisan storage:link
   ```

## Running the Application

1. **Start Laravel Development Server:**

   ```bash
   php artisan serve
   ```

## Directory Structure

Here’s an overview of the essential directories:

```
fit-fold-data
├── app               # Laravel application logic (models, controllers, etc.)
├── artisan           # Laravel command-line interface file
├── bootstrap         # Laravel framework bootstrap files
├── composer.json     # Composer dependencies configuration file
├── config            # Laravel configuration files
├── database          # Database migrations, seeders, and factories
├── public            # Publicly accessible files (entry point for Laravel)
├── python            # Directory containing Python scripts
│   ├── fit-cal-water-model.py # Script for fitting DSC data
│   ├── fit-helicity-degree-large-N.py # Script for fitting helicity degree (large N)
│   ├── fit-helicity-degree-small-N.py # Script for fitting helicity degree (small N)
│   ├── read-cal-data.py      # Script for reading DSC data
│   ├── read-data.py          # Script for reading CD data
│   └── requirements.txt      # Python dependencies for the project
├── resources         # View templates and raw assets (SASS, JavaScript)
├── routes            # API and web routes
├── storage           # Logs, compiled views, and cache files
├── tests             # PHP unit and feature tests
├── vendor            # Composer dependencies (to be installed by composer install command)
└── .env              # Environment configuration file
```