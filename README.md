# Lebo Davies | OnlyBrands

The website for **https://lebodavies.com**, rebuilt from the old Wix site as plain HTML and CSS. There's no build step, and it's hosted free on GitHub Pages.

## Files

- `index.html`: the home page (About, OnlyBrands, Gallery)
- `404.html`: shown for any address that doesn't exist
- `assets/css/style.css`: all styling
- `assets/js/main.js`: mobile menu and the gallery's full-size photo view
- `assets/img/`: photos (WebP), logo and icons
- `assets/video/`: videos
- `CNAME`: the custom domain (`lebodavies.com`)
- `robots.txt`, `sitemap.xml`: help search engines find the site

## Hosting

GitHub Pages publishes this branch automatically (**Settings → Pages**). Any change pushed here is live within a minute or two.

DNS is at Porkbun: four A records point to `185.199.108–111.153`, and `www` is a CNAME to `tradepad.github.io`. `lebodavies.co.za` (GoDaddy) forwards to `lebodavies.com`.

## Adding photos

Resize new photos to about 1600 px on the long side and save them as WebP (for example with squoosh.app). Put them in `assets/img/`, then copy one of the `<a>…</a>` lines in the gallery in `index.html`.
