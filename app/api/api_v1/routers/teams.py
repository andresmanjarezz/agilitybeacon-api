from fastapi import APIRouter, Request, Depends, Response
import typing as t

from app.db.session import get_db
from app.db.teams import models
from app.db.core import (
    get_lists,
    get_item,
    create_item,
    delete_item,
    edit_item,
    soft_delete_item,
)
from app.db.teams.schemas import (
    TeamCreate,
    TeamEdit,
    TeamOut,
)
from app.core.auth import get_current_active_user

team_router = r = APIRouter()


@r.get(
    "/teams",
    response_model=t.List[TeamOut],
)
async def teams_list(
    request: Request,
    response: Response,
    db=Depends(get_db),
):
    """
    Get all teams
    """
    teams = get_lists(db, models.Team, request.query_params)
    response.headers["Content-Range"] = f"0-9/{len(teams)}"
    return teams


@r.get(
    "/teams/{team_id}",
    response_model=TeamOut,
)
async def team_details(
    team_id: int,
    db=Depends(get_db),
):
    """
    Get any team details
    """
    return get_item(db, models.Team, team_id)


@r.post("/teams", response_model=TeamOut)
async def team_create(
    team: TeamCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new team
    """
    team.created_by = current_user.id
    return create_item(db, models.Team, team)


@r.put("/teams/{team_id}", response_model=TeamOut)
async def team_edit(
    team_id: int,
    team: TeamEdit,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Update existing team
    """
    team.updated_by = current_user.id
    return edit_item(db, models.Team, team_id, team)


@r.delete(
    "/teams/{team_id}",
    response_model=TeamOut,
)
async def team_delete(
    team_id: int,
    db=Depends(get_db),
):
    """
    Delete existing team
    """
    return soft_delete_item(db, models.Team, team_id)
