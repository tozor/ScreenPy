#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Setup script for easy ScreenPy installation.
#  
#  Copyright 2018 Aleksey Slucenko <dev@oleksa.me>
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
#  
#  

from setuptools import setup

setup(
    name='ScreenPy',
    description='Script for uploading screenshots to the dropbox',
    version='0.0.2',
    scripts=['screenpy'],
    install_requires=['dropbox']
)
