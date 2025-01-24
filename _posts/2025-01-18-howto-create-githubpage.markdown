---
layout: post
title: How to Create a GitHub Page
thumbnail: \public\img\githubpage.png
---

GitHub Pages is a free service that allows you to host websites directly from your GitHub repository. Follow this step-by-step guide to create your GitHub Page.

![img](\public\img\github.png)

## Step 1: Set Up a GitHub Repository
1. Log in to GitHub: Go to [GitHub](https://github.com/) and log in to your account.
2. Create a New Repository:
    * Click the + button in the top-right corner and select New repository.
    * Enter a repository name (e.g., `my-portfolio`).
    * Set the repository to Public (required for GitHub Pages).
    * Check Add a README file.
    * Click Create repository.

## Step 2: Add Your Website Files
1. Clone the repository to your local machine:
```
bash
git clone https://github.com/<your-username>/<repository-name>.git
```
2. Add your website files (e.g., `index.html`, `style.css`, and images) to the repository folder.
3. Commit and push the changes:
```
bash
git add .
git commit -m "Add website files"
git push
```

## Step 3: Enable GitHub Pages
1. Go to the Settings tab of your repository.
2. Scroll down to the Pages section (on the left sidebar or under "Code and Automation").
3. Under Branch, select the branch you want to publish (usually `main`) and click Save.
4. GitHub will display the URL where your site is hosted, typically:
```
https://<your-username>.github.io/<repository-name>/
```

## Step 4: Test Your Website
1. Open the URL provided in the GitHub Pages section.
2. Verify that your website is displayed correctly.

## Step 5: Customize Your Website (Optional)
Enhance with Jekyll:
* GitHub Pages supports Jekyll, a static site generator. Add a `_config.yml` file to customize themes, plugins, and layouts.

## Step 6: Maintain and Update Your Site
1. Update your website files locally.
2. Push changes to the repository:
```
bash
git add .
git commit -m "Update website content"
git push
```
3. Changes will automatically reflect on your GitHub Page.

## Additional Tips
* Check Themes: GitHub offers built-in themes for Jekyll sites. Go to Settings > Pages > Change Theme.
* Add SEO: Include a `robots.txt` and `sitemap.xml` for search engine optimization.
* Monitor Traffic: Use Google Analytics or similar tools to track visitors.
