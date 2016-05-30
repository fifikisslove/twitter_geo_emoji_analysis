###Parameters

An idea is to collect only these. 

```
"coordinates": null,
"created_at": "Mon Sep 24 03:35:21 +0000 2012",
"text": "Aggressive Ponytail #freebandnames",
"friends_count":32
```

Very simple but includes coordinates, time of creation and the actual text. It might be an idea to only extract emojis directly, instead of saving all of the text.

Should save a lot of space and I believe we have all the we need for analysis. We can analyse emojis according to time and place. But of course this is only a suggestion.

I found all the parameters [here](https://dev.twitter.com/rest/reference/get/search/tweets), under example result.

####Formatting

This is how we get the information from Twitter. All are stolen from [here](https://dev.twitter.com/overview/api/tweets), where a little bit more information can also be found.

######coordinates:

```
"coordinates":
{
    "coordinates":
    [
        -75.14310264,
        40.05701649
    ],
    "type":"Point"
}
```

######created at:

```
"created_at":"Wed Aug 27 13:08:45 +0000 2008"
```

######text:

```
"text":"Tweet Button, Follow Button, and Web Intents javascript now support SSL http:\/\/t.co\/9fbA0oYy ^TS"
```
