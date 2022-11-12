from rest_framework import serializers

from main.models import Bb, Comment

class BbSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at')

class BbDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at',
                    'contacts', 'image')
                    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'content', 'author', 'created_at')
        
class BbSerializer(serializers.HyperlinkedModelSerializer):
    comment_set = serializers.HyperlinkedRelatedField(many=True, 
                view_name='comment-detail', read_only=True)
    
    class Meta:
        model = Bb
        fields = ('url', 'title', 'content', 'price', 'created_at',
                    'contacts', 'image', 'comment_set')


        
