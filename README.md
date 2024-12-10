# Ado playlist

The admin has hidden the flag as a song within this playlist, can you find it?

# How to run (if you want to)

```
docker compose up --build
```

## Notes

- The chromium takes a while to load
- Try not to DoS by refreshing the page a billion times since the images and audio need to be retransmitted
- The flag format is `rwandiCTF{([a-z_])+}` (i.e. `rwandiCTF{}` with lowercase letters and underscore only)

## Hints/Tips

If want hints, scroll down, they are given one at a time
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

1. To solve this, you will need a server with a public URL. [Tunnelmole](https://github.com/robbie-cahill/tunnelmole-client) is a simple tool to give your locally running HTTP(s) servers a public URL. To set up a URL that forwards to `localhost:8000`, use:

```
tmole 8000
```
You can make a server with `flask` that runs on port 8000.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

2. In the images, loading is set to lazy. This basically means that images are only loaded if they are a certain distance away from the bottom of the screen.

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

3. The list is being sorted with the flag