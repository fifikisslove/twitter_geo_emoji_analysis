###Parameters

An idea is to collect only these. 

```
"coordinates": null,
"created_at": "Mon Sep 24 03:35:21 +0000 2012",
"text": "Aggressive Ponytail #freebandnames",
"geo": null,
```

Very simple but includes coordinates and geo (not sure about the difference), time of creation and the actual text. It might be an idea to only extract emojis directly, instead of saving all of the text.

Should save a lot of space and I believe we have all the we need for analysis. We can analyse emojis according to time and place. But of course this is only a suggestion.

I found all the parameters [here](https://dev.twitter.com/rest/reference/get/search/tweets), under example result.
