#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  uvesafb.py
#
#  Copyright 2013 Antergos
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

""" VESA driver installation """

from hardware.hardware import Hardware
import os

CLASS_NAME = "VesaFB"
CLASS_ID = "0x0300"

# All modern cards support Vesa. This will be used as a fallback.
DEVICES = []

class VesaFB(Hardware):
    def __init__(self):
        pass

    def get_packages(self):
        return ["v86d", "xf86-video-vesa"]

    def post_install(self, dest_dir):
        pass

    def check_device(self, class_id, vendor_id, product_id):
        """ Checks if the driver supports this device """
        # All modern cards support Vesa. This will be used as a fallback.
        if class_id == CLASS_ID:
            return True
        else:
            return False
