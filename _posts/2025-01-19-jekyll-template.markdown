---
layout: post
title: How to Customize a GitHub Page Using Jekyll Template
thumbnail: \public\apple-touch-icon-144-precomposed.png
---

GitHub Pages integrates seamlessly with [Jekyll](https://jekyllrb.com/), a static site generator, allowing you to create and customize professional websites easily. Follow this step-by-step guide to set up and customize your page using a Jekyll template.

## Step 1: Enable Jekyll on Your GitHub Page
1. Create a Repository:
    * Go to [GitHub](https://github.com/).
    * Create a new repository and name it (e.g., `my-blog`).
    * Add a README.md file and set the repository to Public.
2. Enable GitHub Pages:
    * Go to the Settings tab of your repository.
    * Navigate to the Pages section.
    * Under Branch, select `main` or another branch you want to publish from, then click Save.
3. Select a Jekyll Theme:
* Under Settings > Pages, click Change Theme.
* Browse the available Jekyll themes and click Select Theme to apply.

## Step 2: Clone the Repository Locally
1. Clone your repository to your local machine:
  ```
  bash
  git clone https://github.com/<your-username>/<repository-name>.git
  ```

2. Navigate to the cloned directory:
  ```
  bash
  cd <repository-name>
  ```

## Step 3: Install Jekyll Locally (Optional)
Installing Jekyll locally allows you to preview changes before pushing them to GitHub.

### Install Prerequisites:

* Install Ruby (latest stable version).
* Install the Bundler and Jekyll gems:
  ```
  bash
  gem install bundler jekyll
  ```

### Set Up Jekyll:
1. Initialize Jekyll in your project:
  ```
  bash
  jekyll new --skip-bundle .
  ```

2. Install dependencies:
  ```
  bash
  bundle install
  ```

3. Preview your site locally:
  ```
  bash
  bundle exec jekyll serve
  ```

Open `http://localhost:4000` to view your site.

## Step 4: Customize Your Jekyll Site
### 1. Edit Configuration (`_config.yml`)
The `_config.yml` file contains global site settings.

Key fields to update:

```
yaml
title: My Jekyll Site
description: A portfolio showcasing my projects
baseurl: "" # Leave empty for GitHub Pages
url: "https://<your-username>.github.io"
author:
  name: Your Name
  email: your-email@example.com
```

### 2. Add or Edit Pages
Create or edit `.html` or `.md` files in the repository:

* `index.md`: The homepage.
* `about.md`: Your "About" page.

Example for an `about.md` file:

```
---
layout: default
title: About Me
---

# About Me

Welcome to my website! I'm passionate about AI and technology. Here, I share my projects and learning journey.
```

### 3. Modify Layouts
* Go to the `_layouts` directory.
* Edit or create custom HTML templates for your pages.
Example `default.html` layout:

```
  <!DOCTYPE html>
  <html>
  <head>
    <title>{{ page.title }}</title>
    <meta name="description" content="{{ site.description }}">
  </head>
  <body>
    <header>
      <h1>{{ site.title }}</h1>
      <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
      </nav>
    </header>
    <main>
      {{ content }}
    </main>
    <footer>
      <p>© {{ site.author.name }} - {{ site.time | date: "%Y" }}</p>
    </footer>
  </body>
  </html>

```

### 4. Add a Blog
1. Create a `_posts` folder.
2. Add blog posts in the format `YYYY-MM-DD-title.md`.

Example blog post:

```
markdown

---
layout: post
title: "My First Blog Post"
date: 2025-01-18
---

# Welcome to My Blog

This is my first post about Jekyll customization!
```

### 5. Customize Styling
1. Add a `assets/css` directory.
2. Create or edit `style.css` and link it in `_config.yml` or layouts:

```
html
<link rel="stylesheet" href="/assets/css/style.css">
```

## Step 5: Push Changes to GitHub
1. Commit and push your updates:
  ```
  bash
  git add .
  git commit -m "Customize Jekyll site"
  git push
  ```

2. Visit your GitHub Page URL to view the updated site.

## Step 6: Advanced Customizations
* Plugins: Add plugins to `_config.yml` for extra features. Example:

```
yaml
plugins:
  - jekyll-seo-tag
  - jekyll-sitemap
```

Install plugins locally with:

```
bash
bundle install
```

* Custom Domain: Add a `CNAME` file to your repository with your custom domain name.

## Step 7: Maintain Your Site
* Update content regularly.
* Test locally before pushing changes.
* Submit your sitemap to search engines for better SEO.
