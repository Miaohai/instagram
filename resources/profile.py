from flask import Response, request, jsonify
from database.models import Profile
from flask_restful import Resource
from urllib.request import urlopen
import json

class ProfilesApi(Resource):
  def get(self):
    profiles = Profile.objects().to_json()
    return Response(profiles, mimetype="application/json", status=200)

  def post(self):
    instagram = 'ysl'
    link='https://www.instagram.com/' + instagram + '/?__a=1'
    page = urlopen(link).read()
    json_data=json.loads(page)
    profile_data=json_data['graphql']['user']
    posts=json_data['graphql']['user']['edge_owner_to_timeline_media']['edges']

    user_profile={
    "username": posts[0]['node']['owner']['username'],
    "num_follower": profile_data['edge_followed_by']['count'],
    "num_followee": profile_data['edge_follow']['count'],
    "num_posts" : profile_data['edge_owner_to_timeline_media']['count'],
    "profile_pic" : profile_data['profile_pic_url'],
    "biography" : profile_data['biography'],
    "is_business_account" : profile_data['is_business_account'],
     "posts" : posts
    }
    body = user_profile
    profile = Profile(**body).save()
    id = profile.id
    return {'id': str(id)}, 200
 
class ProfileApi(Resource):
  def put(self, username):
    body = request.get_json()
    Profile.objects.get(username=username).update(**body)
    return '', 200
 
  def delete(self, username):
    profile = Profile.objects.get(username=username).delete()
    return '', 200

  def get(self, username):
    profiles = Profile.objects.get(username=username).to_json()
    return Response(profiles, mimetype="application/json", status=200)
