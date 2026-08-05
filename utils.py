"""
MCP Server Template - Utility Functions
"""

import httpx
import config


async def call_api(path: str, body: dict = None, params: dict = None) -> dict:
    """Call backend API

    Args:
        path: API path
        body: Request body
        params: Query parameters

    Returns:
        API response data
    """
    url = f"{config.API_BASE_URL}{path}"
    key = config._current_api_key

    headers = {"Content-Type": "application/json"}
    if key:
        headers["X-Api-Key"] = key

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, json=body, params=params, headers=headers)

            # Handle authentication failure
            if resp.status_code == 401:
                return {"code": 401, "msg": "Authentication failed, API key is invalid or expired", "data": None}

            # Handle other non-200 status codes
            if resp.status_code != 200:
                # Only log 500 errors
                if resp.status_code == 500:
                    config.logger.error(f"API {path} returned status code: {resp.status_code}, response: {resp.text[:500]}")

            try:
                data = resp.json()
                return data
            except Exception as json_error:
                # Only log 500 errors
                if resp.status_code == 500:
                    config.logger.error(f"API {path} returned non-JSON response: {resp.text[:500]}")
                return {"code": resp.status_code, "msg": f"API returned non-JSON format, status code: {resp.status_code}", "data": None}
    except Exception as e:
        config.logger.error(f"API {path} request failed: {str(e)}")
        return {"code": 500, "msg": f"API request failed: {str(e)}", "data": None}


def check_response(res: dict, action: str = "query") -> tuple:
    """Check API response, return (success, data_or_error_msg)

    Args:
        res: API response data
        action: Action description

    Returns:
        (success, data_or_error_msg) tuple
    """
    # Handle authentication failure
    if isinstance(res, dict) and res.get("code") == 401:
        return False, f"Authentication failed: {res.get('msg', 'API key is invalid or expired')}, please check X-Api-Key configuration."

    if isinstance(res, dict) and res.get("Message"):
        return False, f"Authentication failed: {res['Message']}, please check X-Api-Key configuration."

    outer_code = res.get("code")
    inner = res.get("data") or {}
    inner_code = inner.get("Code")

    if outer_code != 200 or inner_code != 1000:
        msg = inner.get("Msg") or res.get("msg") or "Unknown error"
        return False, f"{action} failed: {msg}"

    return True, inner


def format_list(data: list, label: str = "", item_formatter=None) -> str:
    """Format a list of items

    Args:
        data: List of items
        label: Label prefix
        item_formatter: Function to format each item

    Returns:
        Formatted string
    """
    if not data:
        return f"{label}No items found." if label else "No items found."

    title = (
        f"{label}Total {len(data)} items:"
        if label
        else f"Total {len(data)} items:"
    )
    lines = [title + "\n"]

    for item in data:
        if item_formatter:
            lines.append(item_formatter(item))
        else:
            lines.append(str(item))
        lines.append("")

    return "\n".join(lines)