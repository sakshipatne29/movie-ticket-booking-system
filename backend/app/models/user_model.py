def user_schema(user):
    return {
    "id": str(user.get("_id")),
    "email": user.get("email"),
    "role": user.get("role")
    }