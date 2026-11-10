import graphene
from graphene_django import DjangoObjectType, DjangoListField
from api.models import Connection, User, PermissionLink
from django.shortcuts import redirect as red
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
import random
def keygen(size):
	return hex(random.getrandbits(size))[2:]





class HandShake(ObjectType):
    """
    Objective:
        This is one of the query which is going to be executed
        The purpose is to get the token from the 3A to authenticate into the website
        If token, doesn't exist
        The redirect Link is generated
        - Redirect to the login page of 3A site
        - Redirect to the permission page for the website
    """
    token = graphene.String()
    redirect = graphene.String()

class DataRequest(DjangoObjectType):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'username']
class Query(ObjectType):
    handshake = graphene.Field(HandShake, domain=graphene.String())
    request = graphene.Field(DataRequest, token=graphene.String())
    # Resolver For Data Request

    def resolve_handshake(root, info, domain):
        """
        Returns token or redirect depending on the user's state
        """
        user = info.context.user
                   
        if user.is_authenticated:
            try:
                print(user)
                con = Connection.objects.get(user=user, domain=domain)
                return HandShake(token=con.token)
            except ObjectDoesNotExist:
                try:
                    permlink = PermissionLink.objects.get(user=user, domain=domain)
                except:
                    permlink = PermissionLink.objects.create(link=f'/permlink/{keygen(256)}', domain=domain, user=user)
                return HandShake(token='', redirect=permlink.link)
        else:
            return HandShake(token="", redirect=red('/'))


    def resolve_request(root, info, token):
        """
        Return The Modified user model to the client website, according the the permissions

        """
        user = info.context.user
        if user.is_authenticated:

            Connection.objects.get(user=user, token=token)
            return user
        
        else:
            raise Exception("User not logged in!")



schema = graphene.Schema(query=Query)