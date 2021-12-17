# meme-template-api
This API is a Meme Template Information. The origin and explanation of Imgflip's top 50 memes are available along with examples for the same. The project is incomplete, only 20/50 meme templates have been updated with information.

To get all meme templates -
```txt
curl get meme-template-api.herokuapp.com/getall
```

To get specific meme templates -
```txt
curl get meme-template-api.herokuapp.com/getone/<meme name>
```

```jsonc
[{"status": "200",
"id": "1",
"title": "Drake Hotline Bling",
"image": "https://i.imgflip.com/30b1gx.jpg",
"explanation": "The meme is a scene from the music video, the object/idea which is not preferred is above and the object/idea which is preferred is below.",
"origin": "Hotline Bling is a 2015 R&B single by the Canadian hip hop artist Drake. Following the release of the song's music video, which features the artist dancing in a color-shifting cube-like structure, it became popular among fans, spawning parodies, remixes, and reaction images often referred to as Drakeposting.",
"popularity": 5,
"tags": ["drake", "hotline", "bling"],
"examples": [
"https://i.pinimg.com/736x/d1/d8/84/d1d884351a4f85b39f51264de2cddae0.jpg",
"https://i.pinimg.com/564x/3e/b1/2c/3eb12c8910b977894c5b2eca7c501a42.jpg",
"https://ultimastatus.com/wp-content/uploads/2021/06/drake-hotline-bling-airplane-seats-memes.jpg"
]
}]
```
