#!/usr/bin/env python
#import os and sys
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "umonya.settings")
    #import from django the execute_from_command_line

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
