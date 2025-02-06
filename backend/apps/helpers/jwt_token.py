from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_token(user):
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token
    
    return {
        'refresh': str(refresh_token),
        'access': str(access_token)
    }