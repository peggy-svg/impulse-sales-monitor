# IMPULSE Sales Monitor

This site records the public `total_sold` field for K-MONSTAR product ID `73504521`. It is **not a verified count of albums sold**, and no private order information is accessed.

## Publish using GitHub Pages

1. Create a new GitHub repository (a **public** repository is the simplest option for GitHub Pages on a free plan). Upload **all files including `.github/workflows/collect.yml`**, preserving the folder structure. Uploading files through GitHub's web interface can be awkward for hidden `.github` directories; using GitHub Desktop or `git push` is more reliable.
2. Go to **Settings → Pages → Build and deployment**. Select **Deploy from a branch**, branch `main`, folder `/ (root)`, then Save.
3. Go to **Settings → Actions → General → Workflow permissions** and select **Read and write permissions** (if available). The workflow must be able to commit to `data/history.json`. If branch protection blocks commits, adjust it or use a dedicated data branch.
4. Go to **Actions → Collect public sales field → Run workflow** to test. Check the logs. If successful, `data/history.json` gains one observation. The public site URL is `https://YOUR-USERNAME.github.io/YOUR-REPO/`.
5. The workflow is scheduled every 15 minutes, but GitHub scheduled jobs may be delayed or skipped. The dashboard checks for new stored data every minute.

## Privacy and limitations

- This is a **link-sharing** site, not a password-protected site. GitHub Pages sites are publicly reachable and may be indexed or shared; the page uses `noindex` as a request to search engines, not access control.
- The repository is public in this setup; anyone with the URL may see the page and data. For real access control, use authenticated hosting or password-protected hosting.
- Only fetch publicly available data at a modest rate. Respect the merchant's terms and any rate limiting; stop collection if the merchant disallows it. Do not bypass login, CAPTCHA, or access controls.
- Cross-origin browser requests are not required: GitHub Actions fetches JSON server-side, and the dashboard reads a local history file.
- `total_sold` may be stale, delayed, or defined differently than the event's album sales. Do not label it as confirmed album quantity.
- If the shop blocks GitHub's servers or changes the JSON structure, the collector will fail safely and retain the previous data.
- On public GitHub repositories, scheduled workflows can be disabled after inactivity; monitor the Actions tab.
