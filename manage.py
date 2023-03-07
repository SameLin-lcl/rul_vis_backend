#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

##  python manage.py inspectdb test_instances test_unit_pca shap_value rul_loss instance_hi model_scores > app/models.py


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vis_rul_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
