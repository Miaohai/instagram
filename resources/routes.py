from .movie import MoviesApi, MovieApi
from .auth import SignupApi
from .profile import ProfilesApi,ProfileApi


def initialize_routes(api):
    api.add_resource(ProfilesApi, '/api/profiles')
    api.add_resource(ProfileApi, '/api/profiles/<username>')
    api.add_resource(SignupApi, '/api/auth/signup')