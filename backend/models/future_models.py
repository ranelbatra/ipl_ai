from pydantic import BaseModel


class UserContext(BaseModel):
    user_id: str | None = None
    username: str | None = None
    subscription: str = "free"


class MatchSelection(BaseModel):
    season: str
    match: str


class AIRequest(BaseModel):
    feature: str
    prompt: str | None = None
    voice_input: bool = False


class FilterRequest(BaseModel):
    team: str | None = None
    player: str | None = None
    venue: str | None = None
    season: str | None = None


class ExportRequest(BaseModel):
    format: str = "pdf"
    include_charts: bool = True


class DashboardRequest(BaseModel):
    user: UserContext | None = None
    match: MatchSelection
    ai: AIRequest | None = None
    filters: FilterRequest | None = None
    export: ExportRequest | None = None