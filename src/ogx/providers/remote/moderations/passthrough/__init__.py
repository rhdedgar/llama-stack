# Copyright (c) The OGX Contributors.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Any

from .config import PassthroughModerationsConfig


async def get_adapter_impl(config: PassthroughModerationsConfig, _deps: Any) -> Any:
    from .passthrough import PassthroughModerationsAdapter

    impl = PassthroughModerationsAdapter(config)
    await impl.initialize()
    return impl
