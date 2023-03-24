# ------------------------------------------------------------------A
# Copyright (c) 2023 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# mscerts is based on certifi and makes the Microsoft Trusted Root
# Program's Certificate Trust Lists available in Python

# See https://github.com/ralphje/mscerts


from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('mscerts')
