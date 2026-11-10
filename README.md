# Third-Party Authentication Service

A Django-based identity provider (IdP) that enables secure third-party authentication for web applications through GraphQL API. This service acts as a centralized authentication hub, allowing external applications to authenticate users without handling sensitive credentials directly.

## Features

- **Custom User Management**: Extended Django user model with profile pictures and third-party account linking
- **GraphQL API**: Modern API interface for authentication handshake and data requests
- **Token-based Authentication**: Secure token system for cross-domain authentication
- **Permission Management**: Granular permission controls for third-party applications
- **Profile Management**: User profile with image upload and management capabilities

## Architecture

### Core Components

- **`src/user_auth/`**: Custom user authentication system with extended user model
- **`src/api/`**: GraphQL API for third-party authentication services
- **`src/third_auth/`**: Django project configuration and URL routing
- **`src/templates/`**: Frontend templates for login and profile pages
- **`src/static/`**: Static assets including CSS, images, and styling

### Database Models

- **User**: Extended authentication model with profile features
- **Connection**: Manages active authentication tokens for third-party domains
- **PermissionLink**: Handles permission requests for new domain connections

## Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment support

### Installation

```bash
# Setup virtual environment and dependencies
make setup

# Activate virtual environment
source .venv/bin/activate

# Navigate to Django project
cd src

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Testing

```bash
# Run all tests
cd src && python manage.py test

# Run specific test
cd src && python manage.py test app.tests.TestClassName.test_method
```

## API Usage

### Authentication Handshake

Query the GraphQL endpoint at `/graphql/` with:

```graphql
query {
  handshake(domain: "https://example.com") {
    token
    redirect
  }
}
```

### User Data Request

```graphql
query {
  request(token: "your-token-here") {
    fname
    lname
    email
    username
  }
}
```

## Security Features

- CSRF protection enabled
- Secure token generation for cross-domain authentication
- Permission-based access control for third-party applications
- Media file handling with image processing and validation

## Technology Stack

- **Backend**: Django 3.1.7 with GraphQL (Graphene)
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Authentication**: Custom Django user model with third-party integration
- **API**: GraphQL with Graphene-Django
- **Frontend**: Django templates with SCSS styling
- **Image Processing**: Pillow for profile picture management

## References
- https://docs.oracle.com/cd/E37459_01/E37463/html/third-party-auth.html
- https://developer.okta.com/docs/concepts/saml/
- https://www.okta.com/identity-101/saml-vs-oauth/#:~:text=SAML%20vs.-,OAuth%3A%20Comparison%20and%20Differences,SAML)%20is%20an%20authentication%20process.&text=Both%20applications%20can%20be%20used,be%20specific%20to%20an%20application
- https://www.secureauth.com/blog/an-introduction-to-saml-security-assertion-markup-language/
- https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
- https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform

- https://www.youtube.com/watch?v=tUqUdu0Sjyc
- https://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/

- https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model

- https://github.com/wsvincent/django-custom-user-model
- https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project/#:~:text=You%20can%20rename%20it%20later%20if%20you%20like.&text=You%20should%20end%20up%20with,%2Fmigrations%2F0001_initial.py.&text=If%20you're%20using%20an,that%20holds%20your%20user%20model.
- https://overiq.com/django-1-10/django-creating-users-using-usercreationform/#:~:text=Here%20we%20are%20defining%20four,default%20widget%20of%20the%20field.

