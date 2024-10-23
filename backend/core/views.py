# DRF Libraries
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Django Libraries
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.http import JsonResponse

# Custom Libraries
from configs.settings import SIMPLE_JWT
from users.models import User
from .models import JsonWebToken as J
from .auths import get_jwt_tokens


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        username = data.get("username")
        password = data.get("password")

        try:
            user_obj = User.objects.get(username=username)
            if user_obj.check_password(password) is False:
                return JsonResponse(
                    {"msg": "존재하지 않는 사용자이거나 비밀번호가 틀렸습니다."},
                    status=401,
                )

            if user_obj.is_active is False:
                return JsonResponse(
                    {"msg": "비활성화된 계정입니다."},
                    status=403,
                )

            print(now())
            print(SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"])

            tokens = get_jwt_tokens(user_obj)
            token_obj = J.objects.create(
                user=user_obj,
                access_token=tokens["access"],
                access_expires_at=now() + SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                refresh_token=tokens["refresh"],
                refresh_expires_at=now() + SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
            )

            user_obj.last_login = now()
            user_obj.save()

            response = {
                "user_id": user_obj.id,
                "access_token": token_obj.access_token,
                "token_idx": str(token_obj.id),
                "msg": "토큰 발급 및 로그인 성공",
            }
            return JsonResponse(response, status=200)

        except User.DoesNotExist:
            return JsonResponse(
                {"msg": "존재하지 않는 사용자이거나 비밀번호가 틀렸습니다."},
                status=401,
            )

        # except Exception as e:
        #     return JsonResponse(
        #         {"msg": f"에러가 발생했습니다. {e}"},
        #         status=500,
        #     )


def logout(request):

    pass


def register(request):
    pass


def change_password(request):
    pass


def reset_password(request):
    pass
