# Django REST Framework — Learning Repository

A structured collection of hands-on exercises for learning **Django REST Framework (DRF)** and the fundamentals of building RESTful APIs with Python and Django.

This repository brings together focused examples of serializers, CRUD operations, API views, authentication, filtering, pagination, throttling, and other core backend concepts. Each directory is intended to explore a particular topic, making it easier to study concepts independently and revisit them when building APIs.

> **Repository type:** Learning and practice repository  
> **Primary focus:** Python backend development, Django REST Framework, and REST APIs

## Table of Contents

- [Overview](#overview)
- [Topics Covered](#topics-covered)
- [Repository Structure](#repository-structure)
- [How DRF Fits Together](#how-drf-fits-together)
- [Getting Started](#getting-started)
- [Running a Practice Module](#running-a-practice-module)
- [Testing APIs](#testing-apis)
- [Learning Goals](#learning-goals)
- [Notes](#notes)

## Overview

Django REST Framework is a toolkit for building Web APIs with Django. This repository contains small, topic-focused projects and experiments that demonstrate how common API features work.

The examples are organized by subject rather than presented as one single production application. This structure helps you focus on one concept at a time—for example, understanding how a serializer validates incoming data before moving on to authentication or pagination.

## Topics Covered

The repository includes practice directories related to the following areas:

| Area | What to explore |
|---|---|
| **Serializers** | Converting model instances and querysets into API-friendly representations, validating incoming data, and handling create/update operations |
| **CRUD operations** | Creating, retrieving, updating, and deleting resources through API endpoints |
| **APIView and class-based APIs** | Organizing request handling with DRF class-based views |
| **ViewSets and ModelViewSet** | Grouping common resource actions and reducing repetitive view code |
| **Serializer relationships** | Exploring related data, nested serializers, and relationship representations |
| **Hyperlinked serializers** | Representing relationships through URLs and hyperlinks |
| **Authentication** | Practising basic, session, token, and JWT-related authentication examples where included |
| **Permissions** | Understanding how API access can be restricted to authenticated or authorized users |
| **Filtering and ordering** | Narrowing results and controlling result order |
| **Pagination** | Splitting large result sets into manageable responses |
| **Throttling** | Applying request-rate limits to API endpoints |
| **Database connectivity** | Exploring database-related practice, including PostgreSQL-oriented examples where configured |

The exact behavior and completeness of each topic depend on the code in its corresponding directory. Refer to that module's source files and settings for implementation details.

## Repository Structure

The repository contains separate directories for individual exercises. The names below reflect the modules currently visible in the repository.

| Directory | Main area |
|---|---|
| `JSONauth/` | JSON/API authentication practice |
| `ViewSet/` | ViewSet-based API patterns |
| `authtoken2/` | Token authentication practice |
| `backendfilter/` | Backend filtering practice |
| `basicauth/` | Basic authentication |
| `classApiView/` | Class-based API views |
| `crud/` | CRUD practice |
| `crudproject/` | CRUD API project |
| `cursorpg/` | PostgreSQL/cursor-related practice |
| `customp/` | Custom implementation practice; inspect source for details |
| `drf1/` – `drf6/` | Progressive DRF exercises |
| `filters/` | Filtering |
| `hyperlinked/` | Hyperlinked serializers/relationships |
| `modelViewSet/` | ModelViewSet patterns |
| `nestedserializers/` | Nested serializers |
| `ordfilter/` | Ordering/filtering practice |
| `pagination1/` | Pagination |
| `pglmoff/` | PostgreSQL/ORM-related practice; inspect configuration for exact scope |
| `serializerRel/` | Serializer relationships |
| `sessionauth/` | Session authentication |
| `sfilter/` | Search/filtering practice |
| `throttling/` | API throttling |
| `tokenauth/` | Token authentication |
| `NOTES.TXT` | Personal study notes on serializers, validation, updates, and token authentication |

**Tip:** These directories are independent learning exercises, not necessarily one integrated Django project. Open the directory you want to study and check for its `manage.py`, settings, app files, and dependencies before running it.

## How DRF Fits Together

A typical request-response flow for a model-backed API looks like this:

```text
Client (browser / frontend / API tool)
                 |
                 | HTTP request + data
                 v
          URL routing
                 |
                 v
        Authentication and
            permissions
                 |
                 v
             API view
                 |
                 v
           Serializer
     (validation / conversion)
                 |
                 v
          Django ORM
                 |
                 v
             Database
                 |
                 v
       Serialized response
          (usually JSON)
                 |
                 v
              Client
```

- **Routing** maps a URL to the appropriate view.
- **Authentication** identifies the requester.
- **Permissions** determine whether the requester may perform the action.
- **Views** coordinate the request and response.
- **Serializers** validate incoming data and convert model instances or querysets into representations suitable for an API.
- **The ORM** provides Django's interface for interacting with the database.

The exact request flow depends on the view, authentication classes, permission classes, and other settings used by an individual module.

## Getting Started

### Prerequisites

Install or prepare:

- Python
- pip
- Basic familiarity with Python and Django
- A terminal or command prompt
- An API client such as HTTPie, `curl`, or Postman
- Any database required by the specific module

### 1. Clone the repository

```bash
git clone https://github.com/finewithpranjal/Django-Rest.git
cd Django-Rest
```

### 2. Create a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Check the selected module for a `requirements.txt` file or documented dependencies. If one is present, install it with:

```bash
python -m pip install -r requirements.txt
```

If no dependency file is provided, install the packages required by that module. A common starting point for a DRF exercise is:

```bash
python -m pip install django djangorestframework
```

Some modules may require additional packages or database drivers. Use the versions and dependencies compatible with that module.

## Running a Practice Module

Because the repository contains multiple exercises, first enter the directory you want to run:

```bash
cd crudproject
```

If that directory contains `manage.py`, install its dependencies and apply migrations if required:

```bash
python manage.py migrate
python manage.py runserver
```

Then open the local development server shown in the terminal, commonly:

```text
http://127.0.0.1:8000/
```

**Important:** Commands and URL paths depend on the selected module. Some exercises may use a different project layout, database configuration, or endpoint. Check the module's `settings.py`, `urls.py`, models, and views before running commands. Do not assume every directory can be launched from the repository root.

## Testing APIs

You can test an endpoint using an API client such as Postman, `curl`, or HTTPie. The exact URL, HTTP method, payload, and authentication header depend on the selected exercise.

Example request structure:

```http
GET /your-api-endpoint/
Accept: application/json
```

Example JSON request body for a create/update endpoint:

```json
{
  "name": "Example Student",
  "roll": 101,
  "city": "Indore"
}
```

The field names above are illustrative. Use the actual fields defined by the selected module's model and serializer.

When testing an endpoint, check:

1. The HTTP method and URL.
2. The request body and content type, when applicable.
3. Authentication and permission requirements.
4. The response status code and JSON body.
5. Validation errors for missing or invalid fields.
6. Database changes after create, update, or delete operations.

For protected endpoints, provide the credentials or token format expected by that module. Never commit real passwords, secret keys, access tokens, or other credentials.

## Learning Goals

This repository is intended to build practical understanding of:

- Designing and working with REST-style endpoints.
- Using serializers for representation and input validation.
- Implementing resource operations with DRF views and ViewSets.
- Understanding authentication separately from permissions.
- Representing related data through serializer relationships.
- Applying search, filtering, ordering, pagination, and throttling.
- Connecting API behavior to Django's ORM and database configuration.
- Testing endpoints and debugging request/response errors.

## Notes

- This is a learning repository made up of focused examples; it should not be assumed to be production-ready.
- Not every module necessarily includes all security, testing, deployment, or error-handling practices required for production.
- Authentication examples may use different approaches. Basic authentication, session authentication, DRF token authentication, and JWT authentication are distinct mechanisms; check each module's configuration before testing it.
- Before deploying any exercise, review `DEBUG`, `ALLOWED_HOSTS`, secret management, database credentials, permissions, throttling, and dependency versions.
- Add or update a module-specific `requirements.txt` when dependencies are known, so another developer can reproduce the environment reliably.

---

**Author:** [Pranjal Malviya](https://github.com/finewithpranjal)  
**Repository:** [finewithpranjal/Django-Rest](https://github.com/finewithpranjal/Django-Rest)
