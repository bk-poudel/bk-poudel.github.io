# Bibek Poudel — Personal Website

Static portfolio website hosted with GitHub Pages.

## Repository structure

```text
.
├── index.html                 # Main portfolio page
├── assets/
│   ├── css/                   # Compiled stylesheets
│   ├── documents/             # Resume and supporting documents
│   ├── icons/                 # Favicon and interface/technology icons
│   ├── images/
│   │   ├── projects/          # Project media, organized by project slug
│   │   └── site/              # Site-wide images
│   ├── js/                    # Browser scripts
│   ├── sass/                  # Stylesheet sources
│   └── webfonts/              # Locally hosted icon fonts
├── projects/                  # Published project pages
├── scripts/                   # Repository maintenance utilities
└── templates/                 # Reusable page templates
```

Public file and directory names use lowercase kebab-case.

## Validate local references

```sh
ruby scripts/validate-links.rb
```

The validator checks local HTML links, media sources, scripts, stylesheets, and CSS `url()` references.
