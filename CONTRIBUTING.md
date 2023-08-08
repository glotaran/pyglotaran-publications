# Contributing Guide

Thank you for your interest in contributing to our list of references! We appreciate the community's involvement, and we're excited to see the list grow with valuable scientific publications.

To keep the list relevant we ask that your entry meets one of the following criteria:
- 📊 A paper in which pyglotaran was used directly.
- 🔬 A reproduction of (part of) the data analysis of a previously published study, which uses pyglotaran.
- 📖 An (in-depth) tutorial or method that involves pyglotaran.

## How to Contribute

We support two methods:
- Contribute via pull request (preferred)
- Contribute by creating an issue

### Contribute via pull request

1. **Fork this repository:**
   Begin by [forking this repository](https://github.com/glotaran/pyglotaran-publications/fork) on GitHub.

2. **Clone Your Fork:**
   After forking, clone your fork to your local machine:

```shell
git clone https://github.com/YOUR_USERNAME/pyglotaran-publications.git
```

3. **Add Your Paper:**
Using the provided template below, add your paper details to the relevant `README.md`. Ensure you replace all placeholders with the correct information about your paper.

4. **Commit Your Changes:**
Commit the changes you've made to your local repository:

```shell
git add README.md
git commit -m "Added paper titled: PAPER_TITLE"
```

5. **Push to Your Fork:**
Push the committed changes to your fork on GitHub:

```shell
git push origin main
```

6. **Open a Pull Request:**
Go to the main repository on GitHub and click on the "New Pull Request" button. Ensure you're comparing your forked `main` branch to the original `main` branch. Fill in the PR template, detailing the paper you added and any other relevant information.

7. **Wait for Review:**
Once you've opened a pull request, our maintainers will review your submission. We may request some changes or improvements. Once everything is in order, your paper will be added to the list!

### Contribute via an issue

1. Open a new issue using the add reference template

2. Edit the (markdown) the issue description to show the reference you wish to add

3. Based on your issue, a maintainer will create a pull request to add the provided details, and `@` you asking to confirm.

4. Once approved and everything is in order, the pull request is merged and your paper will be added to the list!

## Guidelines

- Ensure the paper meets one of the aforementioned criteria, or explain in more details why you think it is a good fit anyway.
- Ensure all links are working and lead to legitimate, safe websites.
- Make sure the paper hasn't been added before to avoid duplicates.
- Use the provided template for consistency.

## Template

Please use the below markdown template, replace the fields in ALL_CAPS with your own text.

```md
---
> ### 📚 **[PAPER_TITLE](PAPER_URL)**
>
> - 📅 **Publication Date:** MONTH DD, YYYY
> - 📘 **Journal:** JOURNAL_NAME
> - 🔗 **DOI:** [DOI_NUMBER](DOI_URL)
>
> [🔍 EG_MORE_DETAILS](URL_1)<br>
> [💻 EG_LINK_2_CODE](URL_2)<br>
>
> ---
>
> #### 🔍 Key Highlights:
>
> ✨ KEY_HIGHLIGHT_1<br>
> ✨ KEY_HIGHLIGHT_2<br>
> ✨ KEY_HIGHLIGHT_3<br>
>
> #### 🔗 Funding | Additional Links:
> YOUR_TEXT_HERE
>
```
