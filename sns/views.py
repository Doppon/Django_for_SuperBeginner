from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Message, Friend, Group, Good

from django.db.models import Q
from django.contrib.auth.decorators import login_required

# indexのビュー関数
@login_required(login_url='/admin/login/')
def index(request):
	# publicのuserを取得
	(public_user, public_group) = get_public()

	# POST送信時の処理

		# Groupsのチェックを更新した時の処理

			# フォームの用意

			# チェックされたGroup名をリストにまとめる

			# Messageの取得

		# Groupsメニューを変更した時の処理

			# フォームの用意

			# Groupのリストを取得

			# メッセージを取得

	# GETアクセス時の処理

		# フォームの用意

		# Groupのリストを取得

		# メッセージの取得

	# 共通処理



def groups(request):
	# 自分が登録したFriendsの取得
	friends = Friend.objects.filter(owner = request.user)

	# POST送信時の処理

		# Groupsメニュー選択肢の処理

			# 選択したGroup名を取得

			# Groupを取得

			# Groupに含まれるFriendを取得

			# FriendのUserをリストにまとめる

			# フォームを用意

		# Friendsのチェック更新時の処理

			# 選択したGroupの取得

			# チェックしたFriendsを取得

			# FriendsのUserを取得

			# Userリストに含まれるユーザーが登録されたFriendを取得

			# すべてのFriendにGroupを設定し保存する

			# メッセージを設定

			# フォームの用意
			
	# GETアクセス時の処理

		# フォームの用意

	# 共通処理


# 投稿をシェアする

	# シェアするMessageの取得

	# POST送信時の処理

		# 送信内容を取得

		# Groupの取得

		# メッセージを作成し、設定をして保存

		# メッセージを設定

	# 共通処理

# goodボタンの処理

	# goodするMessageを取得

	# 自分がメッセージにGoodした数を調べる

	# ゼロより大きければ既にgood済み

	# Messageのgood_countを1増やす

	# Goodを作成し、設定して保存

	# メッセージを設定


# --- 以下、普通の関数 ---	


# 指定されたグループ及び検索文字によるMessageの取得

	# publicの取得

	# チェックされたGroupの取得

	# Groupに含まれるFriendの取得

	# FriendのUserをリストにまとめる

	# UserりすとのUserが作ったGroupの取得

	# groupがgroupsに含まれるか、me_groupsに含まれるMessageの取得

# publicなUserとGroupを取得する
