# Sign in with Apple

* 소셜 로그인을 제공하는 모든 앱들은 애플로 로그인하는 방법을 의무적으로 구현하여야 함.
* 애플은 정적 클라이언트 시크릿을 사용하지 않고 개인키를 사용해 만든 클라이언트 시크릿\(6개월 후 만료\) 을 사용함

## Flow

기본적으로는 일반적인 OAuth2 - Authorization Code 방식

1. authorzation url 을 엔드유저에게 제공해서 grant 요청
2. 애플이 code와 state를 던져주면 OAuth 표준 따라 access token 요청 
3. 원래대로라면... 리소스 서버에 요청을 해야겠지만 애플은 그없. 제공해주는 아이디 토큰을 까서 데이터를 꺼내와야 함

## Links

* [Apple로 로그인 - 앱과 웹사이트에 로그인하는 빠르고 쉬운 방법.](https://developer.apple.com/kr/sign-in-with-apple/)
* [Implementing Sign In with Apple in your Django \(Python\) backend](https://medium.com/@aamishbaloch/sign-in-with-apple-in-your-django-python-backend-b501daa835a9)
* [Understand OAuth 2.0](https://docs.authlib.org/en/v0.12/basic/oauth2.html)
* [Sign in with Apple Tutorial, Part 3: Backend - Token verification \| Sarun](https://sarunw.com/posts/sign-in-with-apple-3/)
* [What the heck is sign in with apple](https://developer.okta.com/blog/2019/06/04/what-the-heck-is-sign-in-with-apple)

