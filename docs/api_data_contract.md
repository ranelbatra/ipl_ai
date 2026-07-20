# Production API Data Contract

## Objective

The current IPL Dashboard API uses simple Pydantic request models for communication between the Streamlit frontend and the FastAPI backend.

As the application evolves, the API should support authentication, AI personalization, query history, voice search, exports, and future AI enhancements without breaking existing functionality.

---

# Current Request Model

The current prototype uses a lightweight request model.

```python
class MatchRequest(BaseModel):
    season: str
    match: str
```

This model is sufficient for local development but cannot support advanced production features.

---

# Design Goals

The production API should:

- Remain backward compatible.
- Support optional future features.
- Minimize frontend changes.
- Keep request validation centralized.
- Be easily extendable.

---

# Production Request Structure

Instead of sending only the selected match, future requests can contain multiple logical sections.

```
Dashboard Request

│

├── User

├── Match

├── AI Settings

├── Filters

└── Export Options
```

---

# Proposed Pydantic Models

## User Information

```python
class UserContext(BaseModel):
    user_id: str | None = None
    username: str | None = None
    subscription: str = "free"
```

Purpose

- Supports authentication
- Stores subscription information
- Enables personalization

---

## Match Selection

```python
class MatchSelection(BaseModel):
    season: str
    match: str
```

Purpose

- Maintains compatibility with the current dashboard.
- Continues to identify the selected IPL match.

---

## AI Request

```python
class AIRequest(BaseModel):
    feature: str
    query: str | None = None
    voice_input: bool = False
```

Purpose

Supports

- AI Detective
- Match Aura
- Documentary Generator
- Team DNA
- Future AI modules

---

## Filter Settings

```python
class FilterRequest(BaseModel):
    team: str | None = None
    venue: str | None = None
    season: str | None = None
    player: str | None = None
```

Purpose

Allows advanced dashboard filtering.

---

## Export Request

```python
class ExportRequest(BaseModel):
    export_type: str = "pdf"
    include_charts: bool = True
```

Purpose

Supports future export functionality.

---

## Dashboard Request

```python
class DashboardRequest(BaseModel):
    user: UserContext | None = None
    match: MatchSelection
    ai: AIRequest | None = None
    filters: FilterRequest | None = None
    export: ExportRequest | None = None
```

This becomes the primary request model for future API communication.

---

# Example Request

```json
{
    "user": {
        "user_id": "123",
        "username": "ranel",
        "subscription": "free"
    },

    "match": {
        "season": "2024",
        "match": "RCB vs CSK"
    },

    "ai": {
        "feature": "ai_detective",
        "query": "Why did RCB lose?",
        "voice_input": false
    },

    "filters": {
        "team": "Royal Challengers Bengaluru"
    },

    "export": {
        "export_type": "pdf",
        "include_charts": true
    }
}
```

---

# Benefits

This production-ready contract provides several advantages:

- Backward compatibility with the existing dashboard.
- Modular request structure.
- Easier maintenance.
- Cleaner API design.
- Future-proof architecture.
- Minimal frontend modifications.
- Simplified feature expansion.

---

# Future Extensions

The data contract can later support:

- Voice Search
- AI Chat
- Saved Reports
- User Preferences
- Query History
- Premium Features
- Notification Settings

without changing the overall request structure.