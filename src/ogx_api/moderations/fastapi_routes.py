# Copyright (c) The OGX Contributors.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Annotated

from fastapi import APIRouter, Body

from ogx_api.router_utils import standard_responses
from ogx_api.version import OGX_API_V1

from .api import Moderations
from .datatypes import ModerationObject
from .models import RunModerationRequest


def create_router(impl: Moderations) -> APIRouter:
    """Create a FastAPI router for the Moderations API."""
    router = APIRouter(
        prefix=f"/{OGX_API_V1}",
        tags=["Moderations"],
        responses=standard_responses,
    )

    @router.post(
        "/moderations",
        response_model=ModerationObject,
        summary="Create Moderation",
        description="Classifies if text inputs are potentially harmful. OpenAI-compatible endpoint.",
        responses={
            200: {"description": "The moderation results for the input."},
        },
    )
    async def run_moderation(
        request: Annotated[RunModerationRequest, Body(...)],
    ) -> ModerationObject:
        return await impl.run_moderation(request)

    return router
