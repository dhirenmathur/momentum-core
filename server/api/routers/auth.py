import json

from fastapi import Depends, Request
from fastapi.responses import JSONResponse, Response

from server.handler.user_handler import user_handler
from server.models.user import CreateUser
from server.utils.APIRouter import APIRouter
from server.utils.user_service import add_users_to_additional_data
from server.utils.test_detail_handler import UserTestDetailsManager
from server.auth import check_auth

auth_router = APIRouter()


@auth_router.post("/signup")
async def signup(request: Request):
    body = json.loads(await request.body())
    user = CreateUser(
    uid= body["uid"],
    email= body["email"],
    display_name= body["displayName"],
    email_verified= body["emailVerified"],
    created_at= body["createdAt"],
    last_login_at= body["lastLoginAt"],
    provider_info= body["providerData"][0],
    provider_username= body["providerUsername"])
    uid, message, error = user_handler.create_user(user)
    add_users_to_additional_data(request, body)
    if error:
        return Response(content=message, status_code=400)

    return Response(content=json.dumps({"uid": uid}), status_code=201)

@auth_router.get("/usage")
async def usage(user=Depends(check_auth)):
    return {"tests_generated": UserTestDetailsManager().get_test_count_last_month(user["user_id"])}