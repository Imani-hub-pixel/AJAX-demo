from .models import UserName,Comment,BlogPost
from rest_framework import serializers

class UserNameCustomeSerializers(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()

    class Meta:
        model=UserName
        fields=['id','first_name','last_name']

    def user_name(self, obj):
        return f'{obj.first_name}+{obj.last_name}'

class CommentSerializer(serializers.ModelSerializer):
    author_name=serializers.CharField(source='author.username',read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'author_name', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id', 'title', 'content', 'author', 'created_at']

    def validate_author(self,obj):
        #self.initial_data-the raw JSON data sent in the api request
        #then extract the comments from the JSON ,no comments return empty list []
        comment_data=self.initial_data.get("comments",[])
        author=obj.get("author") or getattr(self.instance,"author",None)

        for comment in comment_data:
            if comment.get("author")!=author.id:
                raise serializers.ValidationError(
                    "All the comments should have the same outhor as the blog post author"
                )
        return obj
    def create(self,validted_data):
        comments_data=validted_data.pop("comments",[])
        post=BlogPost.objects.create(**validted_data)

        for comment_data in comments_data:
            Comment.objects.create(post=post,**comment_data)

        return post

        
