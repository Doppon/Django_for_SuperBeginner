from django import forms
from.models import Message, Group, Friend, Good
from django.contrib.auth.models import User

# Messageのフォーム(使うときに記述)

# Groupのフォーム(使うときに記述)

# Friendのフォーム(使うときに記述)

# Goodのフォーム(使うときに記述)

# 検索フォーム
class SearchForm(forms.Form):
  search = forms.CharField(max_length=100)

# Groupのチェックボックスフォーム

# Groupの選択メニューフォーム

# Friendのチェックボックスフォーム

# Group作成フォーム

# 投稿フォーム
