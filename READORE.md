deploy は https://www.youtube.com/watch?v=zizzeE4Obc0 を参考に heroku でデプロイした
heroku のデプロイボタンで main ブランチをデプロイする
log の見方は heroku login して
heroku logs --app kasokomi -t
heroku run bash --app kasokomi

heroku config:set --app kosokomi AWS_ACCESS_KEY_ID=AKIAURCGM5YTF2KJAKGG AWS_SECRET_ACCESS_KEY=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


heroku config:set --app kasokomi S3_BUCKET_NAME=kasokomi