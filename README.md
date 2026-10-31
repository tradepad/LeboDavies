# Lebo Davies | OnlyBrands

A static rebuild of the Wix site at https://pad1964.wixsite.com/lebo-davies. Plain HTML and CSS: no Wix, no build step, free to host.

Content (bio, blog post, business description, photos, videos and logo) was taken from the Wix account. The page layout was redesigned, because Wix's layout can't be exported.

## Files

- `index.html`: home page (hero, About, OnlyBrands, Gallery, News, Newsletter)
- `news/opening-soon.html`: the "Opening Soon" blog post
- `assets/css/style.css`, `assets/js/main.js`: styling, mobile menu, gallery lightbox
- `scripts/localize_media.py`: downloads the photos and videos from Wix into the repo

## Before cancelling Wix: save the photos and videos

The photos and videos are still loaded from Wix's servers. They'll keep working while the Wix site exists, even on the free plan. To copy them into the repo, use the GitHub Actions workflow included in the repo:

1. On GitHub, open the repository's **Actions** tab.
2. Choose **Save photos and videos from Wix** in the list on the left.
3. Click **Run workflow**, pick this branch, then click the green **Run workflow** button.

After a minute or two it commits the files to `assets/media/` and updates the pages to use them. To run it on your own computer instead, use `python3 scripts/localize_media.py`.

## Putting it online (free)

**GitHub Pages:** in the repository's settings, open **Pages**, choose **Deploy from a branch**, and pick this branch with the `/ (root)` folder.

Or connect the repository to Netlify or Cloudflare Pages. Neither needs a build command, and the publish directory is `/`.

## Newsletter sign-up

The form is hidden until it has somewhere to send sign-ups. Create a free form at https://formspree.io, then replace `YOUR_FORM_ID` in `index.html`.
