# Copyright (c) The OGX Contributors.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Protocol, runtime_checkable

from .datatypes import ModerationObject
from .models import RunModerationRequest


@runtime_checkable
class Moderations(Protocol):
    """Moderations API for content classification.

    OpenAI-compatible Moderations API endpoint.
    """

    async def run_moderation(self, request: RunModerationRequest) -> ModerationObject:
        """Classify if inputs are potentially harmful."""
        ...
