# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .stack_settings import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "stackmgmt",
  "mod": "index",
  "fqn": "pequod_stackmgmt",
  "classes": {
   "stackmgmt:index:StackSettings": "StackSettings"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "stackmgmt",
  "token": "pulumi:providers:stackmgmt",
  "fqn": "pequod_stackmgmt",
  "class": "Provider"
 }
]
"""
)
