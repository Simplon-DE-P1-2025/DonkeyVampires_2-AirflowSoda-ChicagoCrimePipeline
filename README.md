# 🚔 Chicago Crime Pipeline

> Pipeline DataOps complet · Ingestion → Validation → Transformation → Chargement

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.x-017CEE)](https://airflow.apache.org/)
[![Astro Runtime](https://img.shields.io/badge/Astro%20Runtime-10.5.0-blueviolet)](https://docs.astronomer.io/astro/runtime-release-notes)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Description

Ce projet implémente un pipeline de données DataOps automatisé qui ingère, valide, transforme et charge les données de criminalité de la ville de Chicago via l'API publique [Chicago Data Portal](https://data.cityofchicago.org/resource/ijzp-q8t2.json).

Le pipeline est orchestré avec **Apache Airflow** via **Astro CLI**, les contrôles qualité sont assurés par **Soda Core**, et les données sont stockées dans **PostgreSQL**.

---

## 🏗️ Architecture du pipeline

```
API Chicago Crimes
       │
       ▼
┌─────────────┐
│  Ingestion  │  ← Étape 1 : récupération via requests
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Soda Valid. │  ← Étape 2 : validation données brutes (crimes_raw)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Transformation│ ← Étape 3 : nettoyage et typage (polars)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Soda Valid. │  ← Étape 4 : validation données propres (crimes_clean)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PostgreSQL │  ← Étape 5 : chargement final (crimes_final)
└─────────────┘
```

> 📌 Schéma visuel détaillé à ajouter après implémentation complète

---

## 🛠️ Stack technique

| Outil | Version | Rôle |
|-------|---------|------|
| [Apache Airflow](https://airflow.apache.org/) | 2.x | Orchestration du pipeline |
| [Astro CLI](https://docs.astronomer.io/astro/cli/overview) | latest | Environnement local Airflow |
| [Astro Runtime](https://docs.astronomer.io/astro/runtime-release-notes) | 10.5.0 | Image Docker Airflow |
| [Soda Core](https://docs.soda.io/soda-core/overview-main.html) | 3.3.3 | Contrôle qualité des données |
| [PostgreSQL](https://www.postgresql.org/) | 12.6 | Stockage des données |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | latest | Containerisation |
| [Polars](https://pola.rs/) | latest | Traitement des données (plus rapide que Pandas) |
| [Python](https://www.python.org/) | 3.11 | Langage principal |

---

## 🚀 Installation et lancement

### Prérequis

- Windows 10/11 avec WSL2 (Ubuntu)
- Docker Desktop installé et démarré
- Astro CLI installé dans WSL2

### Étapes

**1. Cloner le repo**
```bash
git clone https://github.com/Simplon-DE-P1-2025/DonkeyVampires_2-AirflowSoda-ChicagoCrimePipeline.git
cd DonkeyVampires_2-AirflowSoda-ChicagoCrimePipeline
```

**2. Créer le fichier `.env`** (ne jamais commiter ce fichier)
```bash
cp .env.example .env
# Remplir les variables dans .env
```

**3. Démarrer l'environnement**
```bash
astro dev start
```

**4. Accéder à l'UI Airflow**
```
URL      : http://localhost:8081
Login    : admin
Password : admin
```

**5. Activer et déclencher le DAG**

Dans l'UI Airflow, activer le DAG `pipeline_chicago_crimes` et cliquer sur ▶️ pour le déclencher manuellement.

### Arrêter l'environnement
```bash
astro dev stop
```

---

## 📁 Structure du projet

```
chicago-crime-pipeline/
├── dags/
│   └── pipeline_chicago_crimes.py   # DAG principal Airflow
├── include/
│   └── soda/
│       ├── configuration.yml         # Connexion Soda → PostgreSQL
│       ├── check_function.py         # Fonction soda_check()
│       └── checks/
│           ├── raw/
│           │   └── crimes_raw.yml    # Checks données brutes
│           └── clean/
│               └── crimes_clean.yml  # Checks données propres
├── plugins/                          # Plugins Airflow custom
├── tests/                            # Tests unitaires
├── Dockerfile                        # Image Astro Runtime 10.5.0
├── requirements.txt                  # Dépendances Python
├── packages.txt                      # Dépendances OS
├── .env.example                      # Template variables d'environnement
└── README.md
```

---

## 🔐 Variables d'environnement

Copier `.env.example` en `.env` et renseigner les valeurs :

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
AIRFLOW__WEBSERVER__WEB_SERVER_PORT=8081
```

> ⚠️ Ne jamais commiter le fichier `.env` — il est dans le `.gitignore`

---

## 👤 Membres de l'équipe

| Nom | Rôle | GitHub |
|-----|------|--------|
| Sabine A. | Data Engineer | [@salamandre910](https://github.com/salamandre910) |

---

## 📊 Checks Soda implémentés

### Données brutes (`crimes_raw`)
- ✅ Volumétrie : `row_count > 1000`
- ✅ Complétude : `missing_count(id) = 0`
- ✅ Fraîcheur : `freshness(date) < 7d`
- ✅ Doublons : `duplicate_count(id) = 0`
- ✅ Coordonnées : `missing_percent(latitude) < 10%`

### Données propres (`crimes_clean`)
- ✅ Volumétrie minimale : `row_count >= 500`
- ✅ Validité arrest : `invalid_percent(arrest) = 0%`
- ✅ Schéma : colonnes `id`, `date`, `primary_type`, `district`
- ✅ Districts valides : `district BETWEEN 1 AND 25`
- ✅ Coordonnées : `missing_percent(latitude) < 5%`

---

## 📝 Licence

Ce projet est sous licence [MIT](LICENSE).

---

*Brief DataOps Simplon · Formation Data Engineer P1 · Mars 2026*
