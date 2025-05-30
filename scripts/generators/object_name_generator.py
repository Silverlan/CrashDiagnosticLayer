#!/usr/bin/python3 -i
#
# Copyright 2023-2025 The Khronos Group Inc.
# Copyright 2023-2025 Valve Corporation
# Copyright 2023-2025 LunarG, Inc.
#
# SPDX-License-Identifier: Apache-2.0

import os
from base_generator import BaseGenerator
from generators.generator_utils import PlatformGuardHelper

class ObjectNameGenerator(BaseGenerator):
    def __init__(self):
        BaseGenerator.__init__(self)

    def generate(self):
        out = []
        out.append(f'''// *** THIS FILE IS GENERATED - DO NOT EDIT ***
// See {os.path.basename(__file__)} for modifications
// Copyright 2023-2025 The Khronos Group Inc.
// Copyright 2023-2025 Valve Corporation
// Copyright 2023-2025 LunarG, Inc.
//
// SPDX-License-Identifier: Apache-2.0
''')
        out.append('''
#pragma once

#ifdef __cplusplus
#include <string>
#endif
#include <vulkan/vulkan.h>
''')
        guard_helper = PlatformGuardHelper()
        out.append(f'static inline const char* string_ObjectName(VkObjectType input_value) {{\n')
        out.append('    switch (input_value) {\n')
        for handle in self.vk.handles.values():
            out.extend(guard_helper.add_guard(handle.protect))
            out.append(f'        case {handle.type}:\n')
            out.append(f'            return "{handle.name}";\n')
        out.extend(guard_helper.add_guard(None))
        out.append('        default:\n')
        out.append(f'            return "UNKNOWN";\n')
        out.append('    }\n')
        out.append('}\n')
        out.append('\n')

        self.write("".join(out))
