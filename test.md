- AppID: AppID_EnvVar
- AppSecret: AppSecret_EnvVar
- URL: http://localhost:5000/
- URLenc: http%3A%2F%2Flocalhost%3A5000%2F

# Facebook Oauth Manual Authentication Flow

## Invoking the Login Dialog and Setting the Redirect URL
### App initiating a redirect to an endpoint which will display the login dialog:

- Application ID from the facebook dev account.
- A redirect URL to which the FB payload will be returned.
- A string value created by the app to maintain state between the request and callback. This parameter should be used for preventing Cross-site Request Forgery and will be passed back, unchanged.
  > https://www.facebook.com/v10.0/dialog/oauth?
      client_id=1913506265471705
      &redirect_uri=http%3A%2F%2Flocalhost%3A5000%2F
      &state=12343242

## Redirect URL with the response code and the state:

> http://localhost:5000/?code=AQBHzsXXHZjaxmTdwUeuLzeM4nSXeVWjx8-Irl3NcZ1S8LjaCFEYoVXT8QZb86PUtociTVYR5BLJVOv4fERATj02Qx3Ei3IYJ5mMl4s-eoihz5XyEDh3qftfCIq8OeeMIlnB4I8PicIP1ayXtHPPmM2VdaMu1k5HMOdhEXWkm0lAe2eQ9O7B_eZkbJRP2NMTtG07K3tbUDGzm6AMvTy0qFK4csZsK-ExHJxlc3K0t3pU5vDyxK_gIPMpIGp1G5XcwPsecbFMqrw-5r6RTkGX3LC70O4N4MQGStdGjNMEJZ9rC8tSBoCpx6k0-wHkXeFr1Sc&state=12343242#_=_

### Code:
> AQBHzsXXHZjaxmTdwUeuLzeM4nSXeVWjx8-Irl3NcZ1S8LjaCFEYoVXT8QZb86PUtociTVYR5BLJVOv4fERATj02Qx3Ei3IYJ5mMl4s-eoihz5XyEDh3qftfCIq8OeeMIlnB4I8PicIP1ayXtHPPmM2VdaMu1k5HMOdhEXWkm0lAe2eQ9O7B_eZkbJRP2NMTtG07K3tbUDGzm6AMvTy0qFK4csZsK-ExHJxlc3K0t3pU5vDyxK_gIPMpIGp1G5XcwPsecbFMqrw-5r6RTkGX3LC70O4N4MQGStdGjNMEJZ9rC8tSBoCpx6k0-wHkXeFr1Sc

## Exchanging Code for an Access Token
### To get an access token, an HTTP GET request to be made to the following OAuth endpoint:

- Application ID from the facebook dev account.
- A redirect URL to which the FB payload will be returned.
- Application secret code set while creating the application in the facebook dev account.
- The code received from FB in the redirect URL in the previous step.

  > https://graph.facebook.com/v10.0/oauth/access_token?
      client_id=1913506265471705
      &redirect_uri=http%3A%2F%2Flocalhost%3A5000%2F
      &client_secret=989fb49bf1853d2410afe53bfbea5c33
      &code=AQBHzsXXHZjaxmTdwUeuLzeM4nSXeVWjx8-Irl3NcZ1S8LjaCFEYoVXT8QZb86PUtociTVYR5BLJVOv4fERATj02Qx3Ei3IYJ5mMl4s-eoihz5XyEDh3qftfCIq8OeeMIlnB4I8PicIP1ayXtHPPmM2VdaMu1k5HMOdhEXWkm0lAe2eQ9O7B_eZkbJRP2NMTtG07K3tbUDGzm6AMvTy0qFK4csZsK-ExHJxlc3K0t3pU5vDyxK_gIPMpIGp1G5XcwPsecbFMqrw-5r6RTkGX3LC70O4N4MQGStdGjNMEJZ9rC8tSBoCpx6k0-wHkXeFr1Sc

### Response:

{
  "access_token": "EAAbMUuU6mtkBALM4QqMfoBbCDL8cEODZBPQktvhK4SjRPpv1PkGht2HyaapR2bL7yc0Di2xOr84l6LiE1w3Bx4Ve0K7iQfZAhwHwDfbWogCX2qvFMBQ1XXZCF1HtZC9vUIqZBC50CB6wZChV82k2mrdRVwL4pDD7kZD", 
  "token_type": "bearer",
  "expires_in":  5183827
}

- access_token: EAAbMUuU6mtkBALM4QqMfoBbCDL8cEODZBPQktvhK4SjRPpv1PkGht2HyaapR2bL7yc0Di2xOr84l6LiE1w3Bx4Ve0K7iQfZAhwHwDfbWogCX2qvFMBQ1XXZCF1HtZC9vUIqZBC50CB6wZChV82k2mrdRVwL4pDD7kZD

### Resource URL:

- Graph API URL.
- Authorization method.
- Fields containing the data that you are trying to get back based on the permissions provided.

> GET https://graph.facebook.com/me?Authorization=Bearer EAAbMUuU6mtkBALM4QqMfoBbCDL8cEODZBPQktvhK4SjRPpv1PkGht2HyaapR2bL7yc0Di2xOr84l6LiE1w3Bx4Ve0K7iQfZAhwHwDfbWogCX2qvFMBQ1XXZCF1HtZC9vUIqZBC50CB6wZChV82k2mrdRVwL4pDD7kZD&fields=name,picture

**JSON Response with Username, and an URL for the picture**
