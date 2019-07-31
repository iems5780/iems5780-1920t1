<<<<<<< HEAD
# Hyde

Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme that pairs a prominent sidebar with uncomplicated content. It's based on [Poole](http://getpoole.com), the Jekyll butler.

![Hyde screenshot](https://f.cloud.github.com/assets/98681/1831228/42af6c6a-7384-11e3-98fb-e0b923ee0468.png)


## Contents

- [Usage](#usage)
- [Options](#options)
  - [Sidebar menu](#sidebar-menu)
  - [Sticky sidebar content](#sticky-sidebar-content)
  - [Themes](#themes)
  - [Reverse layout](#reverse-layout)
- [Development](#development)
- [Author](#author)
- [License](#license)


## Usage

Hyde is a theme built on top of [Poole](https://github.com/poole/poole), which provides a fully furnished Jekyll setup—just download and start the Jekyll server. See [the Poole usage guidelines](https://github.com/poole/poole#usage) for how to install and use Jekyll.


## Options

Hyde includes some customizable options, typically applied via classes on the `<body>` element.


### Sidebar menu

Create a list of nav links in the sidebar by assigning each Jekyll page the correct layout in the page's [front-matter](http://jekyllrb.com/docs/frontmatter/).

```
---
layout: page
title: About
---
```

**Why require a specific layout?** Jekyll will return *all* pages, including the `atom.xml`, and with an alphabetical sort order. To ensure the first link is *Home*, we exclude the `index.html` page from this list by specifying the `page` layout.


### Sticky sidebar content

By default Hyde ships with a sidebar that affixes it's content to the bottom of the sidebar. You can optionally disable this by removing the `.sidebar-sticky` class from the sidebar's `.container`. Sidebar content will then normally flow from top to bottom.

```html
<!-- Default sidebar -->
<div class="sidebar">
  <div class="container sidebar-sticky">
    ...
  </div>
</div>

<!-- Modified sidebar -->
<div class="sidebar">
  <div class="container">
    ...
  </div>
</div>
```


### Themes

Hyde ships with eight optional themes based on the [base16 color scheme](https://github.com/chriskempson/base16). Apply a theme to change the color scheme (mostly applies to sidebar and links).

![Hyde in red](https://f.cloud.github.com/assets/98681/1831229/42b0b354-7384-11e3-8462-31b8df193fe5.png)

There are eight themes available at this time.

![Hyde theme classes](https://f.cloud.github.com/assets/98681/1817044/e5b0ec06-6f68-11e3-83d7-acd1942797a1.png)

To use a theme, add anyone of the available theme classes to the `<body>` element in the `default.html` layout, like so:

```html
<body class="theme-base-08">
  ...
</body>
```

To create your own theme, look to the Themes section of [included CSS file](https://github.com/poole/hyde/blob/master/public/css/hyde.css). Copy any existing theme (they're only a few lines of CSS), rename it, and change the provided colors.

### Reverse layout

![Hyde with reverse layout](https://f.cloud.github.com/assets/98681/1831230/42b0d3ac-7384-11e3-8d54-2065afd03f9e.png)

Hyde's page orientation can be reversed with a single class.

```html
<body class="layout-reverse">
  ...
</body>
```


## Development

Hyde has two branches, but only one is used for active development.

- `master` for development.  **All pull requests should be submitted against `master`.**
- `gh-pages` for our hosted site, which includes our analytics tracking code. **Please avoid using this branch.**


## Author

**Mark Otto**
- <https://github.com/mdo>
- <https://twitter.com/mdo>


## License

Open sourced under the [MIT license](LICENSE.md).

<3
=======
# IEMS 5780 Building and Deploying Scalable Machine Learning Services (2019-2020 Term 1)

## Course Description

Machine learning refers to making computer to perform various tasks by learning from data. It is also now one of the essential components in many online services, such as in generating personalized recommendations on e-commerce platforms, performing face detection and recognition, predicting the arrival time of delivery, etc. Given the widespread usage of machine learning, it is important that complex machine learning models can be deployed in an efficient way to support real time services at scale and to allow seamless update of the models.

This course will introduce basic concepts in computer networking and network programming, and then go ton to introduce how scalable online services can be created and maintained, with a focus on services that nvolve machine learning. Topics will include asynchronous programming, distributed message queues and brokers, load balancers, micro-services, distributed caches and databases, and challenges and solutions in deploying various machine learning models.

---

## Course Details

### Lectures

- **Instructor:** Dr. Albert Au Yeung [cmauyeung@ie]
- **Time:** Every Friday 19:00 - 21:30
- **Venue:** TBC

### Teaching Assistant

- **Teaching Assistant:** TBC

### Assessment Schemes

- **10%** - Attendance
- **60%** - Programming Assignments
- **30%** - Final Examination

---

## Course Materials

- [Slack Group](https://iems5780-1920t1.slack.com/)
- [Lectures](lectures.md)
- [Assignments](assignments.md)

---

## References

### Python Programming
- [Think Python 2nd Edition](https://greenteapress.com/wp/think-python-2e/) by Allen B. Downey. 2015 Green Tea Press
- [The Python (3.6) Tutorial](https://docs.python.org/3.6/tutorial/)

### Machine Learning
- [scikit-learn User Guide](http://scikit-learn.org/stable/user_guide.html)
- [Machine Learning Yearning](http://www.mlyearning.org/) by Andrew Ng

### Scalability
- Guide to Reliable Distributed Systems: Building High-Assurance Applications and Cloud-Hosted Services (Kenneth Birman, 2012)
- Big Data: Principles and best practices of scalable realtime data systems (Nathan Marz &amp; James Warren, 2015)
- Mining of Massive Datasets (Anand Rajaraman, Jeff Ullman &amp; Jure Leskovec, 2011)
- Scalability Rules: 50 Principles for Scaling Web Sites (Martin L. Abbott &amp; Michael T. Fisher, 2011)
>>>>>>> b210b40c2398f5872933ef76418de8d70c2ffbfa
