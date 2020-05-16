# flask-jwt-auth

* based on [Token\-Based Authentication With Flask – Real Python](https://realpython.com/token-based-authentication-with-flask/)
* PyJWTを使ったサンプル
* unittestが秀逸
* User/BlacklistToken model

## セットアップ

### git

make repository called "flask-jwt-auth" first (my original)

```shell
git clone https://github.com/realpython/flask-jwt-auth.git
cd flask-jwt-auth
git checkout tags/1.0.0 -b jwt-auth
git remote set-url origin https://github.com/higebobo/flask-jwt-auth.githttps://github.com/higebobo/flask-jwt-auth.git
```

## config

* TOKEN_EXPIREDがトークンの有効期間
* TestingConfigでは5秒に設定している(test_auth.pyで6秒でタイムアウトさせたいから)

## 全般

unittest

```shell
make test
```

run

```shell
make run
```

認証なしGET

```shell
curl localhost:5000/auth/status
{
  "message": "Provide a valid auth token.", 
  "status": "fail"
}
```

ユーザ登録

```shell
curl -H "Content-Type: application/json" -X POST -d '{"email":"foo@example.com", "password":"bar"}' http://localhost:5000/auth/register
{
  "auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDU1MzE3OTUsImlhdCI6MTU0NTUzMTc5MCwic3ViIjoxfQ.exUCNjK_CZrTMh7DE8QZ3on_ezMXRLX6GZIF1FdBBAg", 
  "message": "Successfully registered.", 
  "status": "success"
}
```

ログイン(token取得)

```shell
curl -H "Content-Type: application/json" -X POST -d '{"email":"foo@example.com", "password":"bar"}' http://localhost:5000/auth/login
{
  "auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDU1NTIzNTYsImlhdCI6MTU0NTU1MjM1MSwic3ViIjoxfQ.7WVqNOEPTmLVRKVupu42VZPLShWO2uIYtP_d_QtaQHY", 
  "message": "Successfully logged in.", 
  "status": "success"
}
```

GET Request with Token

```shell
curl -X GET http://localhost:5000/auth/status -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDU1NTMyNTAsImlhdCI6MTU0NTU1Mjg5MCwic3ViIjoxfQ.Q3eI1C0O8ae1HtVq16oL8fa500jT-sz9p-koln1MkWw"
{
  "data": {
    "admin": false, 
    "email": "foo@example.com", 
    "registered_on": "Sun, 23 Dec 2018 11:23:10 GMT", 
    "user_id": 1
  }, 
  "status": "success"
}
```
