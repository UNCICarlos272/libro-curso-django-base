from django.forms import ModelForm # modelos de django
from .models import Comment # modelo local

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)